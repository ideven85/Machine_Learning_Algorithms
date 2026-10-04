In Graph Neural Networks (GNNs), mini-batching is fundamentally
different from traditional deep learning on images or text because
graphs vary in size, topology, and node connectivity. Standard tensor
stacking into fixed shapes (such as \\(\[B, C, H, W\]\\)) does not work
natively.

Depending on whether you are working with **multiple separate graphs**
or a **single giant graph**, mini-batching is handled in two distinct
ways:

------------------------------------------------------------------------

### 1. Batching Multiple Separate Graphs (Graph-Level Tasks)

*Common in molecular property prediction or protein classification.*

Instead of padding adjacency matrices with zeros (which wastes memory
and computation), frameworks like PyTorch Geometric combine \\(B\\)
separate graphs into a **single, large disjoint graph**:

1.  **Feature Concatenation:** Node feature matrices \\(X_1, X_2,
    `\dots`{=tex}, X_B\\) are concatenated vertically into a single
    large matrix \\(X\_{total} = \[X_1; X_2; `\dots`{=tex}; X_B\]\\).
2.  **Edge Index Shifting:** Edge indices for each graph are shifted by
    cumulative node offsets so that edges only connect nodes within
    their original graph.
3.  **Batch Vector Tracking:** A `batch` vector of shape
    \\(\[N\_{total}\]\\) is generated, storing the graph ID (\\(0, 1,
    `\dots`{=tex}, B-1\\)) for each node. Global pooling (readout)
    operators use this vector to aggregate node embeddings per
    individual graph.

#### PyTorch Geometric Code Example (Multiple Graphs):

``` python
import torch
from torch_geometric.data import Data
from torch_geometric.loader import DataLoader

# Create 2 individual molecular graphs
g1 = Data(x=torch.randn(3, 16), edge_index=torch.tensor([]))
g2 = Data(x=torch.randn(4, 16), edge_index=torch.tensor([]))

# DataLoader merges them into a single disjoint graph batch
loader = DataLoader([g1, g2], batch_size=2)
batch = next(iter(loader))

print(batch.x.shape)  # torch.Size() -> Concatenated 3 + 4 nodes
print(batch.edge_index.shape)  # Shifted edge indices
print(batch.batch)  # tensor() -> Graph ID per node
```

------------------------------------------------------------------------

### 2. Mini-Batch Sampling on a Single Giant Graph (Node/Link Tasks)

*Common in citation networks, social networks, or recommendation systems
where the full graph cannot fit into GPU memory.*

To train on a single multi-million node graph without loading the entire
network at once, sampling algorithms construct localized subgraphs
around a subset of target nodes:

1.  **Target Selection:** A mini-batch randomly selects \\(B\\) target
    nodes (seed nodes) for which predictions will be evaluated.
2.  **Backward \\(K\\)-Hop Expansion:** For a \\(K\\)-layer GNN, the
    algorithm works backward \\(K\\) hops to sample a restricted set of
    neighbors (e.g., 15 neighbors at hop 1, 10 at hop 2).
3.  **Subgraph Extraction:** The sampled nodes and their interconnecting
    edges form a self-contained mini-batch subgraph.
4.  **Loss Masking:** Message passing is run over the entire sampled
    subgraph, but loss and gradients are computed **only on the \\(B\\)
    target nodes** (boundary context nodes have incomplete neighborhoods
    and are masked out).

#### PyTorch Geometric Code Example (`NeighborLoader`):

``` python
import torch
from torch_geometric.data import Data
from torch_geometric.loader import NeighborLoader

# Single large graph
num_nodes = 10000
edge_index = torch.randint(0, num_nodes, (2, 50000))
data = Data(x=torch.randn(num_nodes, 128), edge_index=edge_index, y=torch.randint(0, 5, (num_nodes,)))

# Sample mini-batches: 128 target nodes, 15 neighbors at 1st hop, 10 at 2nd hop
train_loader = NeighborLoader(
    data,
    num_neighbors=,       # 2-layer GNN neighborhood expansion
    batch_size=128,
    input_nodes=torch.arange(1000) # Labeled target training nodes
)

for minibatch in train_loader:
    # minibatch.batch_size contains the first 128 nodes (the targets)
    # minibatch.x contains target nodes + sampled multi-hop neighbors
    out = model(minibatch.x, minibatch.edge_index)
    loss = criterion(out[:minibatch.batch_size], minibatch.y[:minibatch.batch_size])
```

------------------------------------------------------------------------

### Comparison of Batching Techniques

  -----------------------------------------------------------------------
  Approach          Typical           Batch             Memory Scaling
                    Application       Construction      
  ----------------- ----------------- ----------------- -----------------
  **Disjoint        Many separate     Merge graphs into Linear with batch
  Union**           small/medium      block-diagonal    size
                    graphs            adjacency with    
                    (molecules,       `batch` IDs       
                    proteins)                           

  **Neighborhood    Single giant      Expand            Bounded per
  Sampling**        graph (social,    \\(K\\)-hop       target node
                    citation,         sampled           
                    e-commerce)       neighborhood from 
                                      target nodes      

  **Cluster-GCN**   Massive single    Partition graph   Fixed to cluster
                    dense graphs      into dense        size
                                      clusters; batch   
                                      combinations of   
                                      clusters          
  -----------------------------------------------------------------------

💡 *Would you like to explore how Cluster-GCN or GraphSAINT construct
subgraph mini-batches differently from neighbor sampling, or see how
link prediction batching works with negative sampling?*
