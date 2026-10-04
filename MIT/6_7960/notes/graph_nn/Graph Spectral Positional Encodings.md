In Graph Transformers and Graph Neural Networks, **Graph Positional Encodings (PEs)** inject structural and distance awareness directly into node representations [1]. Because standard message passing or self-attention operators can be order-invariant, adding positional encodings helps the model distinguish distinct nodes, evaluate relative structural distances, and incorporate global topology [1, 2].

The two most widely used graph positional encodings are:
1. **Laplacian Positional Encodings (LPE):** Uses the eigenvectors corresponding to the smallest non-zero eigenvalues of the Graph Laplacian \\(L = I - D^{-1/2} A D^{-1/2}\\) to provide global coordinate-like structural embeddings [1].
2. **Random Walk Positional Encodings (RWPE):** Uses the return probabilities \\(P_{vv}^k\\) of a \\(k\\)-step random walk (where \\(P = D^{-1} A\\)) to capture local structural context and node centrality.

---

### Python Code Implementation (PyTorch)

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


# -------------------------------------------------------------------------
# 1. Laplacian Positional Encoding (LPE)
# -------------------------------------------------------------------------
def compute_laplacian_positional_encoding(adj_matrix: torch.Tensor, k: int = 4):
    """
    Computes Laplacian Positional Encodings using the normalized Graph Laplacian:
    L_sym = I - D^{-1/2} A D^{-1/2}

    Args:
        adj_matrix: [N, N] Dense Adjacency matrix
        k: Number of smallest non-trivial eigenvectors to keep
    Returns:
        lpe: [N, k] Matrix containing the k Laplacian eigenvectors
    """
    N = adj_matrix.size(0)

    # Calculate degree matrix D
    deg = adj_matrix.sum(dim=-1)
    deg_inv_sqrt = torch.pow(deg.clamp(min=1e-12), -0.5)
    deg_inv_sqrt[deg == 0] = 0.0

    # Normalized Laplacian L_sym = I - D^{-1/2} A D^{-1/2}
    deg_mat = torch.diag(deg_inv_sqrt)
    L_sym = torch.eye(N, device=adj_matrix.device) - deg_mat @ adj_matrix @ deg_mat

    # Compute eigendecomposition
    eigenvalues, eigenvectors = torch.linalg.eigh(L_sym)

    # Sort eigenvectors by eigenvalues in ascending order
    idx = eigenvalues.argsort()
    eigenvectors = eigenvectors[:, idx]

    # Exclude the first trivial eigenvector (eigenvalue ~ 0) and take next k eigenvectors
    if eigenvectors.size(1) > k:
        lpe = eigenvectors[:, 1 : k + 1]
    else:
        lpe = eigenvectors[:, 1:]

    return lpe


# -------------------------------------------------------------------------
# 2. Random Walk Positional Encoding (RWPE)
# -------------------------------------------------------------------------
def compute_random_walk_positional_encoding(adj_matrix: torch.Tensor, k_steps: int = 4):
    """
    Computes Random Walk Positional Encodings using transition matrix P = D^{-1} A:
    RWPE_v = [P_{vv}^1, P_{vv}^2, ..., P_{vv}^k]

    Args:
        adj_matrix: [N, N] Dense Adjacency matrix
        k_steps: Maximum number of random walk steps
    Returns:
        rwpe: [N, k_steps] Matrix containing diagonal return probabilities
    """
    deg = adj_matrix.sum(dim=-1, keepdim=True).clamp(min=1e-12)
    P = adj_matrix / deg  # Transition matrix P = D^{-1} A

    P_power = P.clone()
    rw_list = []

    for step in range(1, k_steps + 1):
        # Extract diagonal elements P_{vv}^step (landing probability on self after 'step' moves)
        rw_list.append(torch.diagonal(P_power, dim1=-2, dim2=-1).unsqueeze(-1))
        P_power = P_power @ P

    rwpe = torch.cat(rw_list, dim=-1)
    return rwpe


# -------------------------------------------------------------------------
# 3. PyTorch Module: Combining Node Features & Positional Encodings
# -------------------------------------------------------------------------
class GraphFeatureWithPE(nn.Module):
    """
    Projects raw node attributes and positional encodings into a shared
    hidden dimension and merges them (via addition or concatenation).
    """

    def __init__(self, in_features: int, pe_dim: int, hidden_dim: int):
        super().__init__()
        self.fc_x = nn.Linear(in_features, hidden_dim)
        self.fc_pe = nn.Linear(pe_dim, hidden_dim)

    def forward(self, x: torch.Tensor, pe: torch.Tensor):
        """
        x: [N, in_features] Node feature matrix
        pe: [N, pe_dim] Computed positional encoding matrix
        """
        h_x = self.fc_x(x)
        h_pe = self.fc_pe(pe)

        # Additive combination (common in Graph Transformers)
        h_out = h_x + h_pe
        return h_out


# -------------------------------------------------------------------------
# 4. Example Usage
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Define a small 4-node graph
    adj = torch.tensor(
        [
            [0.0, 1.0, 1.0, 0.0],
            [1.0, 0.0, 1.0, 1.0],
            [1.0, 1.0, 0.0, 1.0],
            [0.0, 1.0, 1.0, 0.0],
        ]
    )

    node_features = torch.randn(4, 8)  # 4 nodes, 8 raw features each

    # Compute PEs
    lpe = compute_laplacian_positional_encoding(adj, k=2)
    rwpe = compute_random_walk_positional_encoding(adj, k_steps=3)

    print("Laplacian Positional Encodings (LPE):\n", lpe)
    print("\nRandom Walk Positional Encodings (RWPE):\n", rwpe)

    # Combine with node features
    pe_layer = GraphFeatureWithPE(in_features=8, pe_dim=2, hidden_dim=16)
    combined_inputs = pe_layer(node_features, lpe)
    print(
        "\nFinal Input Embeddings Shape (ready for Transformer/GNN):",
        combined_inputs.shape,
    )
```

---

### Practical Considerations
* **Sign Ambiguity in LPE:** Because Laplacian eigenvectors \\(\phi\\) and \\(-\phi\\) are both valid solutions, models often apply random sign flipping during training (\\(\pm \phi\\)) or learn sign-invariant projections [1].
* **Handling Larger Graphs:** For large graphs, exact Laplacian eigendecomposition is replaced by sparse solvers (such as SciPy's `scipy.sparse.linalg.eigsh`) to calculate the \\(k\\) smallest non-zero eigenvectors efficiently.

💡 *Would you like to explore how these positional encodings are integrated into a multi-head Graph Attention (GAT) layer or a full Graph Transformer architecture?*