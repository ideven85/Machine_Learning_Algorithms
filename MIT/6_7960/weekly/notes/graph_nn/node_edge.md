This is a perfect excerpt to transition from *how* Graph Neural Networks learn (Message Passing and Pooling) to what they actually *do* with what they've learned.

Once a GNN has passed messages around and generated final embeddings for every node, it uses those embeddings to answer specific questions. Here is the breakdown of the two most granular tasks a GNN can perform, starting with the intuition and moving through the math you provided.

### 1. The Intuition First

* **Node-level tasks (Classification/Regression):** Imagine you walk into a massive high school cafeteria. You don't know anyone, but you see a new student sit down at a table surrounded by the chess club. Even without speaking to the new student, you can confidently guess they play chess based on their neighborhood. You are classifying the *node* itself based on its context.
* **Edge prediction tasks (Link Prediction):** Now imagine two students who have never met. However, they both hang out with the exact same group of five friends, take the same math class, and both follow the school's robotics page. Given how similar their networks are, you predict that they *should* know each other. You are predicting a missing *link* (edge) between them.

### 2. The Underlying Maths (Decoding the Excerpt)

The equations in your text describe exactly how the GNN translates final node embeddings into these predictions.

#### Node Classification Equation

> $\text{Pr}(y^{(n)} = 1\vert{}X,A) = \text{sig}(\beta_K + \omega_K h^{(n)}_K)$

Here, $h^{(n)}_K$ is the final embedding of node $n$ after $K$ layers of message passing. The network simply takes this vector, multiplies it by a learned weight $\omega_K$, adds a bias $\beta_K$, and squishes the result through a sigmoid function ($\text{sig}$).

* **What this means:** It is just standard logistic regression applied to the node's final embedding. Because the embedding $h^{(n)}_K$ already contains information about the node's neighbors, the GNN doesn't need to look at the rest of the graph to make this final classification.

#### Edge Prediction Equation

> $\text{Pr}(y^{(mn)} = 1\vert{}X,A) = \text{sig}(h^{(m)T} h^{(n)})$

This equation is wonderfully elegant. To predict an edge between node $m$ and node $n$, we take the **dot product** of their embeddings ($h^{(m)T} h^{(n)}$) and pass it through a sigmoid.

* **What this means:** In linear algebra, a dot product is a measure of similarity. If node $m$ and node $n$ have very similar embeddings (meaning their features and neighborhoods align), their vectors will point in the same direction, making the dot product large. The sigmoid function turns this large number into a probability close to $1$ (100% chance they should be connected).

### 3. Case Studies and Applications

* **Node-Level (Fraud Detection):** Banks use GNNs to analyze transaction networks. A node represents a bank account. Even if an account looks legitimate on paper (good features), if the GNN sees that it frequently sends money to known money-laundering hubs (bad neighborhood), the node is classified as fraudulent.
* **Edge-Level (Recommender Systems):** This is how Pinterest and Amazon work. They map Users and Items as a bipartite graph. If the dot product similarity between User A's embedding and Item B's embedding is high, the GNN predicts an edge, and the system recommends Item B to User A.

### 4. Practical Implementation with Code

Here is how you might implement that exact Edge Prediction dot-product logic in PyTorch using the final embeddings from a GNN:

```python
import torch
import torch.nn as nn


class EdgePredictor(nn.Module):
    def __init__(self):
        super(EdgePredictor, self).__init__()
        self.sigmoid = nn.Sigmoid()

    def forward(self, node_embeddings, edge_indices):
        # node_embeddings: Tensor of shape [num_nodes, embedding_dim] (This is 'h_K')
        # edge_indices: Tensor of shape [2, num_edges_to_predict] (Pairs of m and n)

        # 1. Extract the embeddings for the specific source nodes (m) and target nodes (n)
        source_nodes_m = node_embeddings[edge_indices[0]]
        target_nodes_n = node_embeddings[edge_indices[1]]

        # 2. Compute the dot product between each pair: h^{(m)T} * h^{(n)}
        # We multiply element-wise and then sum across the embedding dimension
        dot_products = (source_nodes_m * target_nodes_n).sum(dim=1)

        # 3. Pass through sigmoid to get probabilities: sig( h^{(m)T} * h^{(n)} )
        probabilities = self.sigmoid(dot_products)

        return probabilities


# Example usage:
# If dot product is high (e.g., 5.0), probability will be ~0.99 (Edge exists)
# If dot product is low/negative (e.g., -2.0), probability will be ~0.11 (No edge)
```

### 5. Terminology

* **Node Embedding ($h_K$):** A dense vector of numbers that captures a node's identity, features, and the structure of its surrounding neighborhood after $K$ layers of message passing.
* **Dot Product Similarity:** A mathematical operation that determines how closely two vectors align in space. Used heavily in AI to measure how "similar" two concepts, words, or graph nodes are.
* **Bipartite Graph:** A graph with two distinct types of nodes (e.g., Users and Movies) where edges only connect a node from one group to a node in the other. Highly common in edge prediction tasks for recommender systems.