In an autoencoder, the objective is to learn a compressed representation (or bottleneck embedding) \\(z = f(x)\\) from which we can reconstruct the original input as closely as possible, yielding \\(\hat{x} = g(z) = g(f(x))\\). 

Because it is often impossible to perfectly invert the encoder, we use a reconstruction loss function to penalize how far the reconstruction \\(\hat{x}\\) is from the original input \\(x\\). The standard choice is the **squared \\(L_2\\) norm (squared Euclidean distance)**:

\\[\mathcal{L}_{\text{recon}}(x, \hat{x}) = \|x - \hat{x}\|_2^2 = \sum_i (x_i - \hat{x}_i)^2\\]

There are several key theoretical, mathematical, and historical reasons why the squared error is the foundational loss metric for autoencoders:

---

### 1. Probabilistic Grounding: The Gaussian Assumption
From an information-theoretic and generative modeling perspective, objective functions are derived by assuming probability distributions to handle uncertainty. 

If we assume that the reconstructed data point \\(\hat{x}\\) deviates from the original input \\(x\\) due to additive, independent, and identically distributed (i.i.d.) **Gaussian noise**, then maximizing the likelihood of the input data under this model leads directly to the **\\(L_2\\) loss**. In other words, minimizing the squared error is mathematically equivalent to finding the maximum likelihood estimate of the network's parameters under a Gaussian noise assumption.

---

### 2. Historical Equivalence to Principal Component Analysis (PCA)
If an autoencoder's encoder (\\(f\\)) and decoder (\\(g\\)) are both restricted to be **linear functions**, minimizing the squared reconstruction error forces the bottleneck embeddings to span the exact same \\(M\\)-dimensional subspace as **Principal Component Analysis (PCA)**. 

Historically, PCA is formulated to maximize the variance captured in a projected subspace, which can be proved to be analytically identical to minimizing the squared Euclidean reconstruction error (\\(L_2\\) distance). Therefore, a deep, non-linear autoencoder using the squared reconstruction loss is fundamentally a **non-linear generalization of PCA**.

---

### 3. Rate-Distortion Theory (Information Bottleneck)
As per **Rate-Distortion Theory**, an autoencoder must compress input data under a limited bottleneck capacity. Minimizing a distortion metric (\\(D\\)) encourages the model to retain as much mutual information as possible about the input distribution. 

By defining the distortion metric as the squared reconstruction error, the loss acts as a practical **surrogate** to maximize the lower bound of mutual information \\(I(X; \hat{X})\\). Minimizing this distortion ensures that the bottleneck discards task-irrelevant noise while compressing and preserving the core structural properties of the input data.

---

### 4. Mathematical and Optimization Convenience
Autoencoders are typically trained using gradient descent and backpropagation. The squared \\(L_2\\) loss is highly advantageous for optimization because:
* It is **smooth and continuously differentiable** everywhere, unlike the \\(L_1\\) loss (absolute error), which has a non-differentiable point at zero.
* It penalizes **larger errors quadratically** while being more forgiving of very small errors, which pushes the optimization process to aggressively correct outliers and align the global structure of the reconstructed data.

***

🧩 Would you like to write a quick Python script using PyTorch or TensorFlow to train a simple autoencoder and visualize how this \\(L_2\\) loss transforms a dataset over training epochs?

Yes, **Principal Component Analysis (PCA)** is fundamentally a dimensionality reduction technique designed to exploit the correlation (relationship) between features to compress data.

When multiple features in a dataset are highly related, they contain redundant information. PCA reorganizes this space by projecting the data onto a lower-dimensional coordinate system that preserves the maximum possible variance.

---

### 1. The Geometric Intuition: Redundancy vs. Nuance
When features are highly correlated, plotting them reveals a clear directional trend.
* **The Dominant Signal (PC1)**: PCA identifies the axis of maximum variation in the data. For example, if you have two highly correlated features \\(r_1\\) and \\(r_2\\), the primary diagonal direction captures almost all of their shared information. This direction is the first **Principal Component (PC1)**, which serves as a highly useful, compact representation.
* **The Discarded Nuance (PC2)**: The direction orthogonal to PC1 represents the remaining variance. In highly correlated datasets, this direction contains very little signal and is treated as negligible "nuance" or noise. PCA discards these lower-variance components, reducing the dimensionality of the representation space while retaining the core structure.

---

### 2. PCA as a Linear Autoencoder
From a representation learning perspective, PCA is mathematically equivalent to a **linear autoencoder with an orthogonal constraint**.

We can map the mechanics of PCA directly onto the encoder-decoder framework:
1. **The Encoder (\\(W\\))**: Projects the raw \\(d\\)-dimensional input vector \\(x\\) onto a lower \\(k\\)-dimensional latent space of the largest principal components:
   \\[z = Wx\\]
   where \\(W\\) is a \\(k \times d\\) matrix.
2. **The Decoder (\\(W^\top\\))**: Projects the compressed code \\(z\\) back into the original \\(d\\)-dimensional space to reconstruct the input:
   \\[\hat{x} = W^\top z = W^\top W x\\]
   where \\(W^\top\\) acts as the decoder.
3. **The Orthogonal Constraint**: PCA constrains the projection matrix to be orthonormal:
   \\[WW^\top = I_{k \times k}\\]
   This ensures that the coordinates in the reduced latent space are completely uncorrelated (orthogonal).

---

### 3. Equivalence of Objectives
Under these linear and orthogonal constraints, PCA minimizes the **squared \\(L_2\\) reconstruction loss** between the input \\(x\\) and its reconstruction \\(\hat{x}\\):
\\[\min_W \mathbb{E} \|x - W^\top W x\|_2^2 \quad \text{s.t.} \quad WW^\top = I\\]

By expanding this quadratic objective, minimizing the reconstruction error is mathematically identical to **maximizing the variance captured** in the projected subspace.

Because of this, if you train a vanilla linear autoencoder (like the `LinearAutoEncoder` we designed earlier) *without* an explicit orthogonal constraint, the weight matrix \\(W\\) will not necessarily be orthogonal, but the learned latent bottleneck \\(z\\) will still **span the exact same \\(k\\)-dimensional subspace** as scikit-learn's PCA.

***

📐 We can write a quick PyTorch and scikit-learn script to compress a dataset, train your `LinearAutoEncoder`, and plot the learned bottleneck side-by-side with classical PCA to visually prove that they span the exact same subspace. Would you like to do that?