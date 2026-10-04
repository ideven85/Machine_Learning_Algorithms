Edge prediction (also called link prediction) shifts the focus from the node itself to the relationships between nodes. It asks: *"Given the current graph, what is the probability that a connection exists—or will exist—between Node A and Node B?" \#diary Just left arm needs a new setup of table hurts when typing long time.. Holding me back..*

## **Concept to Intuition**

Imagine you join Zachary's Karate Club. You become friends with the instructor (Mr. Hi), and you also become friends with three other students who train under him.  
If we look at the graph, you and the instructor share many mutual friends. Intuition (and human sociology) tells us that people with mutual friends are highly likely to become friends themselves. This is called **triadic closure** (if A knows B, and B knows C, A is likely to know C).  
Edge prediction is the machine learning version of this intuition. The Graph Neural Network (GNN) learns the "neighborhood signature" of every node. If it sees that two nodes have very similar signatures—meaning they operate in the same social circles or structural roles—it predicts a high probability that an edge should exist between them.

## **Underlying Mathematics**

In graph-level or node-level tasks, you use the GNN to output a classification directly. For edge prediction, the GNN is only the *first half* of the architecture (the Encoder). You need a *second half* (the Decoder) to evaluate the edges.

> 1. **The Encoder (GNN):** First, you run a standard GNN (like GCNConv) over the graph to generate node embeddings.  
   * Node \$u\$ gets embedding vector \$z\_u\$  
   * Node \$v\$ gets embedding vector \$z\_v\$  
> 2. **The Decoder (Similarity metric):** To predict an edge between \$u\$ and \$v\$, you combine their embeddings to generate a single score. The most common method is the **Dot Product**:  
>    \$\$s\_{u,v} \= z\_u \\cdot z\_v\$\$  
>    Because the GNN puts structurally similar nodes close together in the vector space, a high dot product mathematically proves they are highly aligned.  
> 3. **The Probability:** We pass that raw score through a Sigmoid function (\$\\sigma\$) to squash it between 0 and 1:  
>    \$\$\\hat{y}\_{u,v} \= \\sigma(s\_{u,v})\$\$  
> 4. **The Loss (BCE):** Since an edge either exists (1) or doesn't (0), this is treated as binary classification using Binary Cross Entropy loss.

## **Case Studies**

> * **Zachary's Karate Club (Sociology):** During the famous 1970s study, a conflict caused the karate club to split in two. Edge prediction algorithms on this graph can accurately predict not just who was friends with whom, but *which faction* a member would join based on the gravity of their connections.  
> * **Recommendation Systems (User-Item Graphs):** If Node A is "You" and Node B is "A pair of running shoes", Amazon uses edge prediction to decide if they should show you the ad. If the probability of an edge forming (a purchase) is high, the recommendation is served.  
> * **Knowledge Graph Completion (Drug Repurposing):** Medical researchers map biological entities as a graph. Node A is an existing drug, Node B is a disease. If the algorithm predicts an edge labeled \[TREATS\] between them, researchers have a new lead for drug repurposing.

## **Practical Implementation**

In PyTorch Geometric (PyG), you train edge prediction by giving the model a mix of "Positive Edges" (connections that actually exist) and "Negative Edges" (random connections that do not exist), forcing it to learn the difference.

Python  
import torch  
import torch.nn.functional as F  
from torch\_geometric.datasets import KarateClub  
from torch\_geometric.nn import GCNConv  
from torch\_geometric.utils import negative\_sampling

\# 1\. Load the Karate Club Dataset  
dataset \= KarateClub()  
data \= dataset\[0\]

\# 2\. Define the Encoder (GNN)  
class GNNEncoder(torch.nn.Module):  
    def \_\_init\_\_(self, in\_channels, out\_channels):  
        super().\_\_init\_\_()  
        self.conv1 \= GCNConv(in\_channels, 16\)  
        self.conv2 \= GCNConv(16, out\_channels)

    def forward(self, x, edge\_index):  
        x \= self.conv1(x, edge\_index).relu()  
        return self.conv2(x, edge\_index) \# Outputs node embeddings (z)

\# 3\. Define the Decoder (Dot Product)  
def predict\_edge(z, edge\_index):  
    \# edge\_index is a 2xN tensor \[source\_nodes, target\_nodes\]  
    source\_nodes \= edge\_index\[0\]  
    target\_nodes \= edge\_index\[1\]  
      
    \# Take the embeddings for the sources and targets  
    z\_source \= z\[source\_nodes\]  
    z\_target \= z\[target\_nodes\]  
      
    \# Dot product: element-wise multiplication followed by sum along columns  
    return (z\_source \* z\_target).sum(dim=-1)

model \= GNNEncoder(dataset.num\_features, out\_channels=8)  
optimizer \= torch.optim.Adam(model.parameters(), lr=0.01)

\# \--- Training Loop \---  
model.train()  
for epoch in range(100):  
    optimizer.zero\_grad()  
      
    \# 1\. Get Node Embeddings  
    z \= model(data.x, data.edge\_index)  
      
    \# 2\. Positive Edges (Real edges from the Karate Club)  
    pos\_edge\_index \= data.edge\_index  
    pos\_pred \= predict\_edge(z, pos\_edge\_index)  
      
    \# 3\. Negative Edges (Random fake edges to teach the model what a "0" looks like)  
    neg\_edge\_index \= negative\_sampling(  
        edge\_index=pos\_edge\_index, num\_nodes=data.num\_nodes,  
        num\_neg\_samples=pos\_edge\_index.size(1))  
    neg\_pred \= predict\_edge(z, neg\_edge\_index)  
      
    \# 4\. Calculate Loss (Binary Cross Entropy)  
    \# True edges should predict 1, Fake edges should predict 0  
    pos\_loss \= F.binary\_cross\_entropy\_with\_logits(pos\_pred, torch.ones\_like(pos\_pred))  
    neg\_loss \= F.binary\_cross\_entropy\_with\_logits(neg\_pred, torch.zeros\_like(neg\_pred))  
      
    loss \= pos\_loss \+ neg\_loss  
    loss.backward()  
    optimizer.step()

## **Terms and Naming Intuition**

> * **Link Prediction / Edge Prediction:** Interchangeable terms. "Link prediction" is an older term originating from studying hyperlinks on the World Wide Web. "Edge prediction" is the formal graph theory term.

> * **Triadic Closure:** "Triad" (three nodes) \+ "Closure" (closing the gap). It is the sociological concept that if a triangle is missing one side (A knows B, B knows C), that side will eventually "close" (A will meet C).  
> * **Negative Sampling:** The GNN needs to know what an edge *isn't*. If you only train it on actual friends, it will assume everyone is friends with everyone. We "sample" a "negative" batch of non-existent edges to act as the 0-class. When doing self supervised learning, augmenting data contrastive way.. To get more data.. But this is only negative.. positive-\> other things-\> graph is perfect for this or no?

Precisely—that line of thinking is spot on.

Within self-supervised graph learning, negative sampling serves as the primary engine driving **contrastive learning**. Since graph structures inherently delineate connected paths (edges) from missing ones (non-edges), they naturally fit contrastive frameworks:

> * **Positive pairs:** Real edges instruct the network to pull corresponding nodes closer within vector space.  
> * **Negative pairs:** Sampled non-edges train the framework to force disconnected entities apart.

Consequently, GNNs extract rich structural signatures without depending on manual supervision.

> * **Dot Product:** Mathematically, a dot product measures how much two vectors point in the exact same direction. If two nodes have a high dot product, it means the GNN has placed them in the exact same mathematical neighborhood.

**Sources**  
1\. [https://github.com/hyein99/CS471\_Pokemon\_battle\_prediction?utm\_source=gemini](https://github.com/hyein99/CS471_Pokemon_battle_prediction?utm_source=gemini)