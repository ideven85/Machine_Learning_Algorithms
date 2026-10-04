## Representation Learning for Large-Scale Recommender Systems  
MG  
  
written by AI  
  
Mattia Gaggi  
February 1, 2026 · 20 min read  
Recommender systems must model complex relationships between users, items, and contextual signals. At scale — hundreds of millions of users, tens of millions of items — these systems face a fundamental retrieval problem: how do you score billions of (user, item) pairs in real time?  
Traditional approaches relied heavily on hand-crafted features and collaborative filtering matrices. Modern production systems instead learn latent representations directly from interaction data, then exploit geometric structure in the embedding space for fast retrieval.  
This post walks through the architecture of a two-tower embedding model, how to train it with negative sampling, how to serve it with approximate nearest neighbor retrieval, and how to evaluate it with ranking metrics.  
The Two-Tower Architecture  
The dominant paradigm for large-scale candidate retrieval is the two-tower model (also called a dual encoder). The idea is simple: encode users and items into a shared embedding space using two independent neural networks, then score relevance via dot product or cosine similarity.  
The key insight behind two-tower models is decomposability: because the user and item encoders are independent, you can pre-compute all item embeddings offline and serve retrieval as a nearest-neighbor lookup against the user embedding at request time.  
Here is the architecture at a high level:  
```
┌─────────────────┐                                     ┌─────────────────┐
│  User Features   │                                     │  Item Features   │
│  (age, history,  │                                     │  (title, genre,  │
│   device, ctx)   │                                     │   price, tags)   │
└────────┬────────┘                                     └────────┬────────┘
         │                                                       │
         ▼                                                       ▼
┌─────────────────┐                                     ┌─────────────────┐
│   User Tower     │                                     │   Item Tower     │
│  ┌─────────────┐ │                                     │  ┌─────────────┐ │
│  │ Embedding   │ │                                     │  │ Embedding   │ │
│  │ Layers      │ │                                     │  │ Layers      │ │
│  ├─────────────┤ │                                     │  ├─────────────┤ │
│  │ FC + ReLU   │ │                                     │  │ FC + ReLU   │ │
│  ├─────────────┤ │                                     │  ├─────────────┤ │
│  │ FC + ReLU   │ │                                     │  │ FC + ReLU   │ │
│  ├─────────────┤ │                                     │  ├─────────────┤ │
│  │ L2 Normalize│ │                                     │  │ L2 Normalize│ │
│  └─────────────┘ │                                     │  └─────────────┘ │
└────────┬────────┘                                     └────────┬────────┘
         │                                                       │
         ▼                                                       ▼
   ┌───────────┐                                           ┌───────────┐
   │   u ∈ R^d  │───────── Dot Product: s = u · v ────────│   v ∈ R^d  │
   └───────────┘                                           └───────────┘


```
PyTorch Implementation  
```
import torch
import torch.nn as nn
import torch.nn.functional as F


class Tower(nn.Module):
    """A single tower: maps sparse + dense features to an embedding."""

    def __init__(
        self,
        num_sparse_features: int,
        sparse_embed_dim: int,
        dense_input_dim: int,
        hidden_dims: list[int],
        output_dim: int,
    ):
        super().__init__()
        self.sparse_embedding = nn.EmbeddingBag(
            num_sparse_features, sparse_embed_dim, mode="mean"
        )
        mlp_input_dim = sparse_embed_dim + dense_input_dim
        layers = []
        for h in hidden_dims:
            layers.append(nn.Linear(mlp_input_dim, h))
            layers.append(nn.ReLU())
            layers.append(nn.BatchNorm1d(h))
            mlp_input_dim = h
        layers.append(nn.Linear(mlp_input_dim, output_dim))
        self.mlp = nn.Sequential(*layers)

    def forward(
        self, sparse_ids: torch.Tensor, sparse_offsets: torch.Tensor,
        dense_features: torch.Tensor,
    ) -> torch.Tensor:
        sparse_emb = self.sparse_embedding(sparse_ids, sparse_offsets)
        x = torch.cat([sparse_emb, dense_features], dim=1)
        x = self.mlp(x)
        # L2 normalize so dot product = cosine similarity
        return F.normalize(x, p=2, dim=1)


class TwoTowerModel(nn.Module):
    """Two-tower retrieval model with temperature-scaled dot product."""

    def __init__(self, user_tower: Tower, item_tower: Tower, temperature: float = 0.05):
        super().__init__()
        self.user_tower = user_tower
        self.item_tower = item_tower
        # Learnable temperature for scaling logits
        self.log_temperature = nn.Parameter(
            torch.tensor(temperature).log()
        )

    def forward(
        self,
        user_sparse_ids, user_sparse_offsets, user_dense,
        item_sparse_ids, item_sparse_offsets, item_dense,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        user_emb = self.user_tower(user_sparse_ids, user_sparse_offsets, user_dense)
        item_emb = self.item_tower(item_sparse_ids, item_sparse_offsets, item_dense)
        temperature = self.log_temperature.exp()
        # Scaled dot product: higher temperature → softer distribution
        logits = torch.matmul(user_emb, item_emb.T) / temperature
        return logits, user_emb, item_emb


```
A few things to note about this implementation:  
* L2 normalization on the tower outputs constrains embeddings to the unit hypersphere. This stabilizes training and makes the dot product equivalent to cosine similarity.  
* The temperature parameter controls the sharpness of the softmax distribution over candidates. Lower temperature makes the model more confident; higher temperature smooths the distribution. We make it learnable so the model can adapt during training.  
* **EmbeddingBag** with mode="mean" efficiently handles multi-valued categorical features (e.g., a user’s interaction history as a bag of item IDs).  
* Training with In-Batch Negative Sampling  
* In a typical training setup, each batch contains B (user, item) positive pairs. Instead of explicitly sampling negatives, we treat all other items in the batch as negatives for each user. This gives us B positives and B * (B - 1) negatives per batch — a technique called in-batch negative sampling.  
* In-batch negatives are computationally free: you already computed the item embeddings, so you just reuse them. The catch is sampling bias — popular items appear more often as negatives, which can push the model toward under-recommending popular content.  
```
def in_batch_softmax_loss(
    logits: torch.Tensor,
    popularity_correction: torch.Tensor | None = None,
) -> torch.Tensor:
    """
    Compute softmax cross-entropy loss with in-batch negatives.

    Args:
        logits: (B, B) matrix of user-item dot products.
                logits[i, j] = score(user_i, item_j).
                Diagonal entries are positive pairs.
        popularity_correction: optional (B,) log-probability of each item
                               under the sampling distribution, used to
                               correct for popularity bias.
    Returns:
        Scalar loss.
    """
    if popularity_correction is not None:
        # Subtract log(p(item)) to debias popular items appearing as negatives
        logits = logits - popularity_correction.unsqueeze(0)

    # Labels: diagonal entries are the positive pairs
    labels = torch.arange(logits.size(0), device=logits.device)
    return F.cross_entropy(logits, labels)


```
The popularity_correction term addresses the sampling bias problem. If item j appears in the batch with probability proportional to its popularity p_j, then the corrected logit becomes s(u, v) - log(p_j). This is equivalent to importance weighting and was introduced in the YouTube recommendations paper (Yi et al., 2019).  
Training Loop  
```
def train_epoch(model, dataloader, optimizer, device):
    model.train()
    total_loss = 0.0

    for batch in dataloader:
        user_sparse = batch["user_sparse_ids"].to(device)
        user_offsets = batch["user_sparse_offsets"].to(device)
        user_dense = batch["user_dense"].to(device)
        item_sparse = batch["item_sparse_ids"].to(device)
        item_offsets = batch["item_sparse_offsets"].to(device)
        item_dense = batch["item_dense"].to(device)
        item_log_freq = batch.get("item_log_frequency")

        logits, _, _ = model(
            user_sparse, user_offsets, user_dense,
            item_sparse, item_offsets, item_dense,
        )

        pop_correction = item_log_freq.to(device) if item_log_freq is not None else None
        loss = in_batch_softmax_loss(logits, popularity_correction=pop_correction)

        optimizer.zero_grad()
        loss.backward()
        # Gradient clipping prevents embedding collapse
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(dataloader)


```
Serving: ANN Retrieval with FAISS  
Once trained, the item tower produces an embedding for every item in the catalog. At serving time, you compute the user embedding on the fly and retrieve the top-K nearest items using approximate nearest neighbor (ANN) search. Exact brute-force search is O(N) per query — unacceptable when N is in the tens of millions. ANN indices trade a small amount of recall for orders-of-magnitude speedup.  
FAISS (Facebook AI Similarity Search) is the standard library for this. The typical production setup uses an IVF (inverted file) index with product quantization for compression:  
```
import numpy as np
import faiss


def build_faiss_index(
    item_embeddings: np.ndarray,
    n_clusters: int = 4096,
    n_subquantizers: int = 16,
    n_bits_per_code: int = 8,
    use_gpu: bool = False,
) -> faiss.Index:
    """
    Build an IVF-PQ index for fast approximate nearest neighbor search.

    Args:
        item_embeddings: (N, D) float32 array of item embeddings.
        n_clusters: number of Voronoi cells for the inverted file.
        n_subquantizers: number of sub-vectors for product quantization.
                         Must divide D evenly.
        n_bits_per_code: bits per sub-quantizer (8 = 256 centroids per subspace).
        use_gpu: whether to use GPU for index building and search.

    Returns:
        Trained FAISS index ready for search.
    """
    dim = item_embeddings.shape[1]

    # IVF with product quantization: fast search + compressed storage
    quantizer = faiss.IndexFlatIP(dim)  # inner product for L2-normalized vectors
    index = faiss.IndexIVFPQ(
        quantizer, dim, n_clusters, n_subquantizers, n_bits_per_code,
        faiss.METRIC_INNER_PRODUCT,
    )

    if use_gpu:
        res = faiss.StandardGpuResources()
        index = faiss.index_cpu_to_gpu(res, 0, index)

    # Train the quantizer on the item embeddings
    index.train(item_embeddings)
    index.add(item_embeddings)

    return index


def retrieve_candidates(
    index: faiss.Index,
    user_embedding: np.ndarray,
    top_k: int = 500,
    n_probe: int = 64,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Retrieve top-K candidate items for a user.

    Args:
        index: trained FAISS index.
        user_embedding: (1, D) or (D,) user embedding vector.
        top_k: number of candidates to retrieve.
        n_probe: number of Voronoi cells to search (trade-off: speed vs recall).

    Returns:
        (scores, item_ids): arrays of shape (top_k,).
    """
    index.nprobe = n_probe

    if user_embedding.ndim  1:
        user_embedding = user_embedding.reshape(1, -1)

    scores, item_ids = index.search(user_embedding, top_k)
    return scores[0], item_ids[0]


```
==A few practical notes on FAISS tuning:==  
* **==n_probe==**== is the most important knob at serving time. Higher values improve recall at the cost of latency. In production, we typically sweep n_probe against a recall target (e.g., 95% recall@100 relative to brute force) and set it to the smallest value that hits the target.==  
* ==Product quantization compresses each D-dimensional vector into n_subquantizers * n_bits_per_code / 8 bytes. For D=128 with 16 subquantizers and 8 bits, that is 16 bytes per vector — a 32x compression over float32.==  
* ==For catalogs over ~100M items, consider IndexIVFPQ with OPQ (optimized product quantization) or a hierarchical approach (HNSW + PQ).==  
* ==Sequential Recommendation==  
* ==User preferences evolve over time. While the two-tower model captures static preferences, sequential models capture the dynamics of user behavior by modeling the ordered sequence of interactions.==  
* ==Common architectures include:==  
* ==SASRec (Self-Attentive Sequential Recommendation): applies a causal Transformer to the user’s interaction history, treating each item as a token. The last hidden state becomes the user embedding.==  
* ==GRU4Rec: uses gated recurrent units over session-level interaction sequences.==  
* ==BERT4Rec: uses a bidirectional masked-item prediction objective (analogous to BERT’s masked language modeling) for learning item representations.==  
* ==In practice, sequential signals are often incorporated as features within the two-tower framework — for example, by feeding the user’s last-N interacted item embeddings through a small Transformer or attention layer inside the user tower, rather than building a standalone sequential model.==  
* ==Graph-Based Approaches==  
* ==Interactions between users and items naturally form a bipartite graph. Graph neural networks (GNNs) propagate information across this structure, enabling each node to aggregate information from its neighborhood.==  
* ==PinSage (Ying et al., 2018) demonstrated that GNN-based embeddings could scale to billions of nodes by using random-walk-based neighborhood sampling and efficient mini-batch training. The key advantages:==  
* ==Cold-start performance: new items with limited interaction data can still get reasonable embeddings by aggregating information from their content features and graph neighbors.==  
* ==Higher-order relational modeling: multi-hop message passing captures patterns like “users who liked X also liked Y, and Y is similar to Z.”==  
* ==Inductive generalization: content-based GNNs can produce embeddings for items never seen during training.==  
* ==Evaluation: Ranking Metrics==  
* ==Evaluating a retrieval model requires ranking-aware metrics. The two most common are NDCG (Normalized Discounted Cumulative Gain) and Hit Rate (Recall@K).==  
```
import numpy as np


def ndcg_at_k(
    predicted_item_ids: np.ndarray,
    ground_truth_ids: set[int],
    k: int,
) -> float:
    """
    Compute NDCG@K for a single query.

    Args:
        predicted_item_ids: ranked array of predicted item IDs (most relevant first).
        ground_truth_ids: set of relevant item IDs.
        k: cutoff rank.

    Returns:
        NDCG@K score in [0, 1].
    """
    predicted = predicted_item_ids[:k]
    # Binary relevance: 1 if item is in ground truth, 0 otherwise
    relevances = np.array([1.0 if iid in ground_truth_ids else 0.0 for iid in predicted])

    # DCG: sum of relevance / log2(rank + 1)
    discounts = np.log2(np.arange(2, len(relevances) + 2))
    dcg = np.sum(relevances / discounts)

    # Ideal DCG: all relevant items ranked first
    ideal_relevances = np.sort(relevances)[::-1]
    n_ideal = min(len(ground_truth_ids), k)
    ideal_discounts = np.log2(np.arange(2, n_ideal + 2))
    idcg = np.sum(np.ones(n_ideal) / ideal_discounts)

    if idcg  0:
        return 0.0
    return dcg / idcg


def hit_rate_at_k(
    predicted_item_ids: np.ndarray,
    ground_truth_ids: set[int],
    k: int,
) -> float:
    """
    Compute Hit Rate (Recall@K): fraction of relevant items retrieved in top K.
    """
    predicted = set(predicted_item_ids[:k].tolist())
    if len(ground_truth_ids) == 0:
        return 0.0
    return len(predicted & ground_truth_ids) / len(ground_truth_ids)


def evaluate_retrieval(
    model: "TwoTowerModel",
    index: "faiss.Index",
    eval_data: list[dict],
    k_values: list[int] = [10, 50, 100],
    device: str = "cpu",
) -> dict[str, float]:
    """
    Evaluate retrieval quality across multiple cutoffs.

    Args:
        model: trained two-tower model.
        index: FAISS index built from item embeddings.
        eval_data: list of dicts, each with user features and ground_truth_item_ids.
        k_values: list of K cutoffs to evaluate.

    Returns:
        Dict of metric_name → score.
    """
    import torch

    model.eval()
    metrics = {f"{m}@{k}": [] for k in k_values for m in ["ndcg", "hit_rate"]}

    with torch.no_grad():
        for sample in eval_data:
            user_emb = model.user_tower(
                sample["user_sparse_ids"].to(device),
                sample["user_sparse_offsets"].to(device),
                sample["user_dense"].to(device),
            ).cpu().numpy()

            _, retrieved_ids = index.search(user_emb, max(k_values))
            retrieved_ids = retrieved_ids[0]
            gt = sample["ground_truth_item_ids"]

            for k in k_values:
                metrics[f"ndcg@{k}"].append(ndcg_at_k(retrieved_ids, gt, k))
                metrics[f"hit_rate@{k}"].append(hit_rate_at_k(retrieved_ids, gt, k))

    return {name: float(np.mean(vals)) for name, vals in metrics.items()}


```
A representative set of results from a production-scale experiment on an e-commerce dataset might look like:  

| METRIC       | TWO-TOWER (OURS) | MF BASELINE | ITEM-KNN |
| ------------ | ---------------- | ----------- | -------- |
| NDCG@10      | 0.142            | 0.098       | 0.071    |
| NDCG@100     | 0.203            | 0.151       | 0.112    |
| Hit Rate@10  | 0.231            | 0.167       | 0.119    |
| Hit Rate@100 | 0.487            | 0.389       | 0.298    |
| p99 Latency  | 4.2ms            | 3.1ms       | 12.8ms   |
  
  
The two-tower model does not just improve relevance metrics — it fundamentally changes the system architecture. By decoupling user and item computation, you move from O(N) scoring at request time to O(1) embedding computation + O(log N) ANN lookup. This is what makes it practical to serve recommendations over catalogs with hundreds of millions of items.  
Practical Considerations  
A few lessons from putting these systems into production:  
1. Embedding dimensionality: 64–256 dimensions is the sweet spot. Higher dimensions improve model capacity but increase serving cost (memory, latency). We typically start at 128 and ablate.  
2. Feature freshness: the user tower’s input features must be fresh at serving time. If you feed in a user’s last-50 interactions but the feature store only updates hourly, the user embedding lags behind their actual behavior. Real-time feature pipelines are not optional.  
3. Index refresh cadence: item embeddings change when you retrain the model. You need a pipeline to re-encode all items, rebuild the FAISS index, and hot-swap it in the serving path — ideally without downtime.  
4. Two-stage architecture: the retrieval model (two-tower + ANN) produces a broad candidate set (typically 100–1000 items). A heavier ranking model — often a cross-attention or feature-interaction model that can jointly attend to user and item features — then re-scores these candidates. Splitting retrieval and ranking is the standard production pattern because it balances coverage with scoring quality.  
5. Future Directions  
6. Large-scale recommender systems are increasingly integrating representation learning, graph modeling, and language models. Recent trends include:  
* LLM-based user modeling: using language models to encode user interaction histories as natural language sequences.  
* Multi-task learning: jointly training retrieval and ranking objectives to align the embedding space with downstream metrics.  
* Generative retrieval: replacing the retrieve-then-rank paradigm with autoregressive models that directly generate item identifiers.  
* The convergence of these approaches is likely to produce more adaptive and context-aware recommendation systems, but the two-tower + ANN architecture remains the production workhorse for the foreseeable future.  
* Mattia Gaggi is an applied machine learning engineer working on production ML systems.  
