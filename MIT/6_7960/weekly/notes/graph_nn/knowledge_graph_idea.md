
# Knowledge Graphs

Here are two foundational paradigms for building and processing Knowledge Graphs in PyTorch: **TransE Knowledge Graph Embeddings** (for link prediction and score evaluation) and a **Relational Graph Convolutional Network (R-GCN)** (for multi-relational message passing across graph entities).

---

### Method 1: Knowledge Graph Embeddings with TransE
The **TransE** architecture represents entities and relations in a continuous vector space where relationships act as translations: \\(h + r \approx t\\).

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# 1. Define Sample Knowledge Graph Triples (Head, Relation, Tail)
entity2id = {
    "Graph Neural Network": 0,
    "Transformer": 1,
    "Knowledge Graph": 2,
    "PyTorch": 3,
    "Representation Learning": 4
}
relation2id = {
    "is_a_type_of": 0,
    "used_for": 1,
    "implemented_in": 2
}

# Triplets: (head, relation, tail)
triplets = torch.tensor([
   ,  # (GNN, is_a_type_of, Representation Learning)
   ,  # (Transformer, is_a_type_of, Representation Learning)
   ,  # (Knowledge Graph, used_for, Representation Learning)
   ,  # (GNN, implemented_in, PyTorch)
   ,  # (Transformer, implemented_in, PyTorch)
], dtype=torch.long)

# 2. TransE PyTorch Module
class TransE(nn.Module):
    def __init__(self, num_entities, num_relations, embedding_dim=16, margin=1.0):
        super(TransE, self).__init__()
        self.margin = margin
        
        # Entity and Relation embedding tables
        self.entity_embed = nn.Embedding(num_entities, embedding_dim)
        self.relation_embed = nn.Embedding(num_relations, embedding_dim)
        
        # Xavier Initialization
        nn.init.xavier_uniform_(self.entity_embed.weight)
        nn.init.xavier_uniform_(self.relation_embed.weight)

    def score(self, h, r, t):
        """Computes translation distance: || h + r - t ||_1"""
        h_emb = F.normalize(self.entity_embed(h), p=2, dim=-1)
        r_emb = self.relation_embed(r)
        t_emb = F.normalize(self.entity_embed(t), p=2, dim=-1)
        return torch.norm(h_emb + r_emb - t_emb, p=1, dim=-1)

    def forward(self, pos_h, pos_r, pos_t, neg_h, neg_r, neg_t):
        """Computes pairwise Margin Ranking Loss with negative sampling"""
        pos_dist = self.score(pos_h, pos_r, pos_t)
        neg_dist = self.score(neg_h, neg_r, neg_t)
        
        # Enforce pos_dist < neg_dist - margin
        loss = F.margin_ranking_loss(
            neg_dist, pos_dist, 
            target=torch.ones_like(pos_dist) * -1, 
            margin=self.margin
        )
        return loss

# 3. Training Setup
num_entities = len(entity2id)
num_relations = len(relation2id)

model = TransE(num_entities, num_relations, embedding_dim=16, margin=1.0)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

heads, rels, tails = triplets[:, 0], triplets[:, 1], triplets[:, 2]

# Training Loop
for epoch in range(1, 201):
    model.train()
    optimizer.zero_grad()
    
    # Generate negative samples by corrupting tail entities
    neg_tails = torch.randint(0, num_entities, tails.shape)
    
    loss = model(heads, rels, tails, heads, rels, neg_tails)
    loss.backward()
    optimizer.step()

print("Training Complete. Model has learned relational vector translations!")
```

---

### Method 2: Multi-Relational Message Passing (R-GCN Layer)
For tasks requiring feature propagation across heterogeneous relationship types, **Relational Graph Convolutional Networks (R-GCN)** apply distinct transformation matrices \\(W_r\\) for each relation type \\(r \in \mathcal{R}\\):

```python
class RGCNLayer(nn.Module):
    """
    Relational Graph Convolutional Layer in native PyTorch.
    Aggregates node embeddings across distinct relation types:
    h_i' = RELU( W_self * h_i + sum_{r} sum_{j in N_i^r} W_r * h_j )
    """
    def __init__(self, in_features, out_features, num_relations):
        super(RGCNLayer, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.num_relations = num_relations
        
        # Relation-specific weight transformation tensors [R, In, Out]
        self.rel_weights = nn.Parameter(torch.Tensor(num_relations, in_features, out_features))
        self.self_weight = nn.Parameter(torch.Tensor(in_features, out_features))
        
        nn.init.xavier_uniform_(self.rel_weights)
        nn.init.xavier_uniform_(self.self_weight)

    def forward(self, x, edge_index, edge_type):
        """
        x: [num_nodes, in_features] - Node feature matrix
        edge_index: [2, num_edges] - Source and destination node indices
        edge_type: [num_edges] - Relation type ID for each edge
        """
        num_nodes = x.size(0)
        out = torch.zeros(num_nodes, self.out_features, device=x.device)
        
        # 1. Transform self-loops
        out += torch.matmul(x, self.self_weight)
        
        # 2. Aggregate incoming messages per relation type
        for r in range(self.num_relations):
            mask = (edge_type == r)
            if not mask.any():
                continue
            
            src, dst = edge_index[0, mask], edge_index[1, mask]
            W_r = self.rel_weights[r]
            
            # Message transformation
            msg = torch.matmul(x[src], W_r)
            
            # Scatter-add messages to target node positions
            out.index_add_(0, dst, msg)
            
        return F.relu(out)

# Example Usage
layer = RGCNLayer(in_features=8, out_features=16, num_relations=3)
node_features = torch.randn(5, 8)  # 5 Knowledge Graph entities
edge_index = torch.tensor([,], dtype=torch.long)
edge_type = torch.tensor(, dtype=torch.long)

updated_embeddings = layer(node_features, edge_index, edge_type)
print("Updated Node Embeddings Shape:", updated_embeddings.shape)
```

---

🕸️ *Would you like to extend this code to handle link prediction scoring for unseen triplets, or build a complete data pipeline that loads RDF/N-Triples files directly?*