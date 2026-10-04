import torch
import torch.nn as nn


class LinearAutoEncoder(nn.Module):
    def __init__(self, d_in: int, d_latent: int):
        super(LinearAutoEncoder, self).__init__()
        # TODO: Define the encoder and decoder
        self.encoder = nn.Linear(d_in, d_latent)
        self.decoder = nn.Linear(d_latent, d_in)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: Implement the forward pass

        return self.decoder(self.encoder(x))

    def compute_loss(self, x: torch.Tensor, x_tilde: torch.Tensor) -> torch.Tensor:
        # TODO: Implement the specific loss function
        return torch.mean(torch.abs(x - x_tilde).pow(2))


def test_linear_autoencoder():
    print("Running LinearAutoEncoder Tests...\n")

    # 1. Setup mock data and hyperparameters
    batch_size = 32
    d_in = 784  # e.g., flattening a 28x28 MNIST image
    d_latent = 16  # Our information bottleneck

    model = LinearAutoEncoder(d_in, d_latent)
    x = torch.randn(batch_size, d_in)  # Mock input batch

    # --- TEST 1: Forward Pass Shape ---
    try:
        x_tilde = model(x)
        assert x_tilde.shape == (batch_size, d_in)
        print("✅ Test 1 Passed: Output shape matches input shape.")
    except AssertionError:
        print(
            f"❌ Test 1 Failed: Expected shape {(batch_size, d_in)}, got {x_tilde.shape}"
        )

    # --- TEST 2: Bottleneck Compression ---
    try:
        latent = model.encoder(x)
        assert latent.shape == (batch_size, d_latent)
        print("✅ Test 2 Passed: Encoder correctly compresses to the latent dimension.")
    except AssertionError:
        print(
            f"❌ Test 2 Failed: Expected latent shape {(batch_size, d_latent)}, got {latent.shape}"
        )

    # --- TEST 3: Loss Computation ---
    try:
        loss = model.compute_loss(x, x_tilde)
        # Check if loss is a scalar (0-dimensional tensor)
        assert loss.ndim == 0
        # MSE of random noise should be strictly positive
        assert loss.item() > 0
        print("✅ Test 3 Passed: Loss evaluates to a valid positive scalar.")
    except AssertionError:
        print(f"❌ Test 3 Failed: Loss computation is incorrect. Got {loss.item()}")

    # --- TEST 4: Gradient Flow (Backpropagation) ---
    try:
        loss.backward()
        # Ensure gradients actually populated in both the encoder and decoder
        assert model.encoder.weight.grad is not None
        assert model.decoder.weight.grad is not None

        # Check that gradients aren't entirely zeroed out
        assert torch.sum(torch.abs(model.encoder.weight.grad)) > 0
        print(
            "✅ Test 4 Passed: Gradients successfully backpropagated through the network."
        )
    except AssertionError:
        print("❌ Test 4 Failed: Gradients did not flow properly.")


# Run the suite
test_linear_autoencoder()
