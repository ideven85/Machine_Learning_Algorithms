Here is a curated set of **5 practice problems** covering Transformer matrix dimensions, attention arithmetic, computational complexity, and positional encodings, based on your notebook sources [1-6]. Complete step-by-step solutions are provided below each question for self-assessment.

---

### **Problem 1: Multi-Head Attention Tensor Shapes & Parameters**
Consider a Transformer layer with the following hyperparameters:
*   Sequence length \\(n = 1024\\)
*   Model embedding dimension \\(d = 768\\)
*   Number of attention heads \\(H = 12\\)
*   Head dimension \\(d_k = d / H = 64\\)

**Questions:**
1. What are the matrix dimensions of the individual Query projection \\(W_q^{(h)}\\), Query matrix \\(Q_h\\), Attention matrix \\(A_h\\), and the combined output projection \\(W^O\\) [1, 2, 7]?
2. How many total learnable weight parameters are in this entire Multi-Head Attention layer (excluding biases) [1, 7]?

<details>
<summary>👉 <b>Click to view Solution 1</b></summary>

**1. Tensor Shapes:**
*   **Query Projection Weight (\\(W_q^{(h)}\\)):** \\(\mathbb{R}^{d \times d_k} = \mathbf{768 \times 64}\\) [1, 2].
*   **Query Matrix (\\(Q_h = X W_q^{(h)}\\)):** \\((n \times d) \times (d \times d_k) = \mathbf{1024 \times 64}\\) [1, 2].
*   **Attention Score Matrix (\\(A_h = \text{softmax}(Q_h K_h^T / \sqrt{d_k})\\)):** \\((n \times d_k) \times (d_k \times n) = \mathbf{1024 \times 1024}\\) [1, 8].
*   **Concatenated Head Matrix (\\(\text{Concat}(Z_1, \dots, Z_H)\\)):** \\(n \times (H \cdot d_k) = \mathbf{1024 \times 768}\\) [1, 2].
*   **Output Projection Weight (\\(W^O\\)):** \\(\mathbb{R}^{H d_k \times d} = \mathbb{R}^{d \times d} = \mathbf{768 \times 768}\\) [1, 2, 7].

**2. Parameter Count:**
*   Each head \\(h\\) has 3 matrices (\\(W_q^h, W_k^h, W_v^h\\)), each of shape \\(d \times d_k\\). Across all \\(H\\) heads, the total parameters for Q, K, and V projections equal:
    \\[\text{Params}_{QKV} = 3 \times H \times (d \times d_k) = 3 \times (H \cdot d_k) \times d = 3 \times d^2 = 3 \times 768^2 = 1,769,472\\]
*   The final fusion matrix \\(W^O\\) has shape \\(d \times d\\):
    \\[\text{Params}_{W^O} = d \times d = 768^2 = 589,824\\]
*   **Total Parameters:** \\(4 \times d^2 = 4 \times 768^2 = \mathbf{2,359,296 \text{ parameters}}\\) [1, 7].
</details>

---

### **Problem 2: Scaled Dot-Product Attention Calculation**
Let \\(d_k = 4\\) (so \\(\sqrt{d_k} = 2\\)). A query vector \\(q\\) and two key vectors \\(k_1, k_2\\) are given as:
\\[q = \begin{bmatrix} 2 \\ 0 \\ -2 \\ 4 \end{bmatrix}, \quad k_1 = \begin{bmatrix} 1 \\ 2 \\ 0 \\ 1 \end{bmatrix}, \quad k_2 = \begin{bmatrix} 0 \\ 0 \\ 2 \\ 2 \end{bmatrix}\\]

**Questions:**
1. Compute the raw dot products \\(q^T k_1\\) and \\(q^T k_2\\).
2. Apply the \\(\frac{1}{\sqrt{d_k}}\\) scaling factor and compute the Softmax attention weights \\(\alpha_1\\) and \\(\alpha_2\\) [3, 9, 10].

<details>
<summary>👉 <b>Click to view Solution 2</b></summary>

**1. Raw Dot Products:**
*   \\(q^T k_1 = (2)(1) + (0)(2) + (-2)(0) + (4)(1) = 2 + 0 + 0 + 4 = \mathbf{6}\\)
*   \\(q^T k_2 = (2)(0) + (0)(0) + (-2)(2) + (4)(2) = 0 + 0 - 4 + 8 = \mathbf{4}\\)

**2. Scaled Scores & Softmax Weights:**
*   Divide by \\(\sqrt{d_k} = 2\\) [3, 10]:
    \\[s_1 = \frac{6}{2} = 3, \quad s_2 = \frac{4}{2} = 2\\]
*   Apply Softmax row-wise [10, 11]:
    \\[\alpha_1 = \frac{e^3}{e^3 + e^2} = \frac{e}{e + 1} \approx \frac{2.718}{3.718} \approx \mathbf{0.731} \quad (73.1\%)\\]
    \\[\alpha_2 = \frac{e^2}{e^3 + e^2} = \frac{1}{e + 1} \approx \frac{1}{3.718} \approx \mathbf{0.269} \quad (26.9\%)\\]
</details>

---

### **Problem 3: Standard Attention vs. Linearized Attention Complexity**
Suppose a long-document transformer processes a sequence length \\(N = 10,000\\) with \\(d = 512\\) and \\(d_k = 64\\).

**Questions:**
1. What is the memory footprint (in number of floating-point values) to store the attention matrix \\(A\\) in standard self-attention [4, 12]?
2. In linearized self-attention using a feature kernel \\(\phi(x)\\), what is the shape and memory size of the context summary matrix \\(\phi(K)^T V\\) [5, 13]?
3. What is the computational time complexity scaling with respect to \\(N\\) for both methods [4, 5]?

<details>
<summary>👉 <b>Click to view Solution 3</b></summary>

**1. Standard Self-Attention Memory:**
*   Standard attention stores an \\(N \times N\\) attention grid per head [4, 12]:
    \\[A \in \mathbb{R}^{N \times N} = 10,000 \times 10,000 = \mathbf{100,000,000 \text{ values (100 million floats) per head}}\\]

**2. Linearized Attention Memory:**
*   By reordering matrix multiplication to compute \\((\phi(K)^T V)\\) first, the context summary matrix has shape \\(d_k \times d_k\\) [5, 13]:
    \\[\phi(K)^T V \in \mathbb{R}^{d_k \times d_k} = 64 \times 64 = \mathbf{4,096 \text{ values (4.096 KB per head)}}\\]
    Notice that this footprint is **completely independent of sequence length \\(N\\)** [5].

**3. Time Complexity Scaling:**
*   **Standard Attention:** \\(\mathcal{O}(N^2 \cdot d)\\) (Quadratic in \\(N\\)) [4, 12].
*   **Linearized Attention:** \\(\mathcal{O}(N \cdot d^2)\\) (Linear in \\(N\\)) [4, 5].
</details>

---

### **Problem 4: Rotary Positional Embedding (RoPE) Invariance**
Let \\(z_m \in \mathbb{C}\\) be a 2D feature pair for a token at position index \\(m\\). Under RoPE, positional encoding is performed via complex multiplication by an angle: \\(\text{RoPE}(z_m, m) = e^{i m \theta} z_m\\) [14].

**Question:**
Prove that the inner product (real part of complex conjugate product \\(\text{Re}(\text{RoPE}(z_m, m) \cdot \overline{\text{RoPE}(w_n, n)})\\)) between two rotated vectors depends strictly on their relative distance \\((m - n)\\) [15].

<details>
<summary>👉 <b>Click to view Solution 4</b></summary>

**Proof:**
1. Express the encoded vectors:
   \\[\text{RoPE}(z_m, m) = e^{i m \theta} z_m, \quad \text{RoPE}(w_n, n) = e^{i n \theta} w_n\\]
2. Take the inner product in complex notation:
   \\[\langle \text{RoPE}(z_m, m), \text{RoPE}(w_n, n) \rangle = \text{Re}\left( (e^{i m \theta} z_m) \cdot \overline{(e^{i n \theta} w_n)} \right)\\]
3. Using the conjugate identity \\(\overline{e^{i n \theta}} = e^{-i n \theta}\\):
   \\[= \text{Re}\left( z_m \cdot \bar{w}_n \cdot e^{i m \theta} e^{-i n \theta} \right) = \text{Re}\left( z_m \cdot \bar{w}_n \cdot e^{i (m - n) \theta} \right)\\]
4. **Conclusion:** The resulting value depends purely on the coordinate vectors \\(z_m, w_n\\) and the position offset \\((m - n)\\), proving relative spatial invariance [15].
</details>

---

### **Problem 5: Causal Masking in Auto-Regressive Attention**
In auto-regressive decoding, a masking matrix \\(M\\) is added to the dot-product matrix before computing Softmax [7, 8]:
\\[A = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)\\]

**Questions:**
1. What specific values are placed in the upper-triangular vs. lower-triangular entries of \\(M\\) [8]?
2. Why must the mask \\(M\\) be added *before* applying the Softmax function rather than after [8]?

<details>
<summary>👉 <b>Click to view Solution 5</b></summary>

**1. Structure of Mask Matrix \\(M\\):**
*   **Lower-triangular entries (including diagonal, \\(j \le i\\)):** set to **\\(0\\)** [8].
*   **Upper-triangular entries (\\(j > i\\)):** set to **\\(-\infty\\)** [8].

**2. Placement Before Softmax:**
*   Softmax exponentiates its input (\\(e^{-\infty} = 0\\)). Adding \\(-\infty\\) before Softmax guarantees that future token attention weights become **exactly \\(0\\)** [8].
*   This normalizes the remaining valid probabilities so that each row still sums to \\(1.0\\), preventing information leakage from future tokens [8].
</details>

---

Would you like to turn these concepts into an **interactive quiz app** or **flashcard deck** in your Studio panel, or dive into another specific Transformer topic?