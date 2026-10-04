Here is a PyTorch implementation of the **GAN minimax game** [1, 2], demonstrating both the theoretical minimax objective and the practical non-saturating generator objective [3].

---

### PyTorch Implementation

```python
import torch
import torch.nn as nn
import torch.optim as optim


# 1. Define Model Architectures
class Generator(nn.Module):
    def __init__(self, latent_dim, data_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, 128), nn.ReLU(), nn.Linear(128, data_dim)
        )

    def forward(self, z):
        return self.net(z)


class Discriminator(nn.Module):
    def __init__(self, data_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(data_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 1),
            nn.Sigmoid(),  # Outputs probability D(x) in [4]
        )

    def forward(self, x):
        return self.net(x)


# Initialize models, loss, and optimizers
latent_dim, data_dim = 100, 784
G = Generator(latent_dim, data_dim)
D = Discriminator(data_dim)

criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer_D = optim.Adam(D.parameters(), lr=2e-4)
optimizer_G = optim.Adam(G.parameters(), lr=2e-4)


# 2. Training Loop
def train_step(real_data, batch_size):
    # Labels for classification
    real_labels = torch.ones(batch_size, 1)  # Label = 1 for real
    fake_labels = torch.zeros(batch_size, 1)  # Label = 0 for fake

    # ----------------------------------------------------
    # Step 1: Optimize Discriminator (Maximize V(D, G))
    # ----------------------------------------------------
    optimizer_D.zero_grad()

    # Loss on real samples: E_x [log D(x)]
    d_real_preds = D(real_data)
    loss_d_real = criterion(d_real_preds, real_labels)

    # Sample noise z ~ N(0, I) and generate fake data G(z)
    z = torch.randn(batch_size, latent_dim)
    fake_data = G(z)

    # Loss on fake samples: E_z [log(1 - D(G(z)))]
    d_fake_preds = D(fake_data.detach())  # Detach G to avoid updating G weights
    loss_d_fake = criterion(d_fake_preds, fake_labels)

    # Total Discriminator Loss (Minimizing BCE is equivalent to Maximizing V(D, G))
    loss_D = loss_d_real + loss_d_fake
    loss_D.backward()
    optimizer_D.step()

    # ----------------------------------------------------
    # Step 2: Optimize Generator (Minimize V(D, G))
    # ----------------------------------------------------
    optimizer_G.zero_grad()

    # Pass fake data through Discriminator again
    d_fake_preds_for_g = D(fake_data)

    # NON-SATURATING LOSS (Recommended in practice):
    # Instead of min log(1 - D(G(z))), maximize log D(G(z)) using real_labels (1)
    loss_G = criterion(d_fake_preds_for_g, real_labels)

    loss_G.backward()
    optimizer_G.step()

    return loss_D.item(), loss_G.item()
```

---

### How the Code Maps to the Minimax Objective

1. **The Discriminator Step (Maximizing \\(V(D, G)\\)):**
   The minimax objective for the discriminator is:
   \\[\max_D \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]\\] [1, 5]
   In PyTorch, `nn.BCELoss` evaluates \\(- [y \log(\hat{y}) + (1-y) \log(1-\hat{y})]\\). Minimizing BCE loss with real labels (\\(y=1\\)) and fake labels (\\(y=0\\)) directly maximizes the discriminator value function [2, 5].

2. **The Generator Step (Non-Saturating Loss vs. Minimax):**
   * **Original Minimax Loss:** \\(\min_G \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]\\) [6, 7]. Early in training when \\(D(G(z)) \approx 0\\), the gradient of \\(\log(1 - D(G(z)))\\) vanishes, leading to slow convergence [6, 7].
   * **Non-Saturating Loss:** \\(\min_G \mathbb{E}_{z \sim p_z}[-\log D(G(z))]\\) [3, 8]. Passing `real_labels` (\\(y=1\\)) to `BCELoss` computes \\(-\log D(G(z))\\), providing a significantly stronger gradient signal early in training [3, 9].

Would you like to explore adding a **Gradient Penalty (WGAN-GP)** [10] to this implementation for improved training stability?