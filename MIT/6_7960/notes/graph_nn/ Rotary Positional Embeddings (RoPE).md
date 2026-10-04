Here is the complete PyTorch implementation of **Multi-Head Attention integrated with Rotary Positional Embeddings (RoPE)** and hardware-optimized via `torch.nn.functional.scaled_dot_product_attention` (SDPA), followed by an overview of RoPE and its modern alternatives.

---

### 1. PyTorch Implementation: RoPE + Scaled Dot-Product Attention

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class RotaryEmbedding(nn.Module):
    """Generates cosine and sine frequency matrices for RoPE."""

    def __init__(self, dim: int, base: float = 10000.0):
        super().__init__()
        self.dim = dim
        self.base = base
        # Compute inverse frequency band across half the feature dimension
        inv_freq = 1.0 / (self.base ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)

    def forward(
        self, x: torch.Tensor, seq_len: int
    ) -> tuple[torch.Tensor, torch.Tensor]:
        t = torch.arange(seq_len, device=x.device, dtype=self.inv_freq.dtype)
        freqs = torch.outer(t, self.inv_freq)  # (seq_len, dim // 2)
        emb = torch.cat((freqs, freqs), dim=-1)  # (seq_len, dim)
        return emb.cos(), emb.sin()


def rotate_half(x: torch.Tensor) -> torch.Tensor:
    """Rotates coordinate pairs: [x1, x2] -> [-x2, x1]."""
    x1 = x[..., : x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2 :]
    return torch.cat((-x2, x1), dim=-1)


def apply_rotary_pos_emb(
    q: torch.Tensor, k: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    """Applies 2D rotation to Query and Key tensors."""
    cos = cos.unsqueeze(0).unsqueeze(0)  # Shape: (1, 1, seq_len, dim)
    sin = sin.unsqueeze(0).unsqueeze(0)
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed


class RoPEMultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model, bias=False)
        self.W_k = nn.Linear(d_model, d_model, bias=False)
        self.W_v = nn.Linear(d_model, d_model, bias=False)
        self.W_o = nn.Linear(d_model, d_model, bias=False)  # W^O fusion matrix

        self.rotary_emb = RotaryEmbedding(dim=self.d_k)

    def forward(self, x: torch.Tensor, is_causal: bool = False) -> torch.Tensor:
        B, N, D = x.shape

        # 1. Project & reshape for parallel heads: (B, N, D) -> (B, H, N, d_k)
        q = self.W_q(x).view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        k = self.W_k(x).view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        v = self.W_v(x).view(B, N, self.num_heads, self.d_k).transpose(1, 2)

        # 2. Generate and apply RoPE to Queries and Keys
        cos, sin = self.rotary_emb(x, seq_len=N)
        q, k = apply_rotary_pos_emb(q, k, cos, sin)

        # 3. Compute Attention using fused FlashAttention/SDPA kernels
        attn_out = F.scaled_dot_product_attention(
            query=q, key=k, value=v, is_causal=is_causal
        )

        # 4. Vectorized Concatenation and W^O projection
        concat_heads = attn_out.transpose(1, 2).contiguous().view(B, N, D)
        return self.W_o(concat_heads)
```

---

### 2. How RoPE Works Mechanically

Unlike standard sinusoidal positional encodings that sum static position vectors \\(p_i\\) directly to token embeddings at the input layer [1, 2]:

* **2D Rotation Matrix:** RoPE divides feature coordinates into 2D pairs \\([x_m^{(1)}, x_m^{(2)}]\\) for a token at position \\(m\\) and rotates them by an angle \\(m\theta\\) using a 2D rotation matrix \\(\begin{pmatrix} \cos m\theta & -\sin m\theta \\ \sin m\theta & \cos m\theta \end{pmatrix}\\) [3].
* **Complex Number Representation:** Equivalently, treating 2D vector pairs as complex numbers \\(z_m := x_m^{(1)} + i x_m^{(2)}\\), applying RoPE simplifies to complex multiplication by an angle: \\(\text{RoPE}(z_m, m) = e^{im\theta} z_m\\) [4].
* **Relative Position Invariance:** Because of rotational trigonometry, the inner product between rotated vectors depends strictly on their relative offset distance \\(m - n\\):
  \\[\text{RoPE}(x, m)^T \text{RoPE}(y, n) = \text{RoPE}(x, m+k)^T \text{RoPE}(y, n+k)\\]
  This property ensures that the attention dot-product reflects the relative distance between tokens rather than their absolute index positions [5].

---

### 3. Alternative & Extension Mechanisms ("Or Better")

* **ALiBi (Attention with Linear Biases):** Rather than modifying token vectors, ALiBi injects an explicit linear distance penalty \\(sB\\) directly into the attention score matrix: \\(\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + sB\right)V\\) [5, 6]. This approach allows pre-training on short context windows while fine-tuning on significantly longer context windows [6].
* **Relative Position Encodings:** Uses a generalized Toeplitz matrix \\(B\\), where bias values \\(B_{i,j}\\) depend purely on index difference \\(i - j\\) [7].
* **Grouped-Query Attention (GQA):** Combines RoPE with a structure where multiple Query heads share single Key and Value heads, reducing memory bandwidth during inference.

---

Would you like to explore how **Grouped-Query Attention (GQA)** or **KV Caching** can be incorporated into this PyTorch pipeline for faster inference? 🚀