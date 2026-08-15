import torch

import torch.nn.functional as F
import math


def clip_symmetric_loss(
    I_f: torch.Tensor, T_f: torch.Tensor, t: torch.Tensor
) -> torch.Tensor:
    N = I_f.shape[0]

    # TODO: 1. L2-normalize the features
    l2_norm = torch.norm(I_f, dim=2)
    # TODO: 2. Compute the scaled pairwise cosine similarities (logits)
    a1 = l2_norm.cos()
    a2 = t.cos()
    distance = a1 * a2

    # TODO: 3. Create the labels (np.arange(n) equivalent in PyTorch)
    torch.arange()
    # TODO: 4. Compute the symmetric cross-entropy loss and return the average


def test_output_shape_and_type():
    """Test that the function returns a single scalar tensor."""
    N, d = 4, 128
    I_f = torch.randn(N, d)
    T_f = torch.randn(N, d)
    t = torch.tensor(1.0)

    loss = clip_symmetric_loss(I_f, T_f, t)

    assert isinstance(loss, torch.Tensor), "Output must be a torch.Tensor"
    assert loss.dim() == 0, f"Expected scalar tensor (0 dimensions), got {loss.dim()}"
    print("test_output_shape_and_type: PASSED")


def test_perfect_alignment():
    """
    If images and texts are perfectly aligned (identical features) and
    temperature is high, the loss should be extremely close to 0.
    """
    N, d = 8, 64
    I_f = torch.eye(N, d)  # Orthogonal, but matching pairs
    T_f = I_f.clone()  # Perfect match
    t = torch.tensor(4.0)  # High temperature to sharpen the softmax

    loss = clip_symmetric_loss(I_f, T_f, t)

    # Loss should be very small (e.g., < 0.01)
    assert (
        loss.item() < 0.01
    ), f"Expected near-zero loss for perfect alignment, got {loss.item()}"
    print("test_perfect_alignment: PASSED")


def test_orthogonal_features():
    """
    If all features are orthogonal to each other, cosine similarities are 0.
    With logits = 0, the softmax distribution is uniform (1/N).
    Cross entropy of a uniform distribution over N classes is ln(N).
    """
    N = 4
    # Create perfectly orthogonal vectors using identity matrix
    I_f = torch.eye(N)
    # Shift T_f so no image matches its corresponding text
    T_f = torch.zeros(N, N)

    # t doesn't matter here since 0 * exp(t) is still 0
    t = torch.tensor(1.0)

    loss = clip_symmetric_loss(I_f, T_f, t)
    expected_loss = math.log(N)

    assert torch.isclose(
        loss, torch.tensor(expected_loss), atol=1e-5
    ), f"Expected {expected_loss}, got {loss.item()}"
    print("test_orthogonal_features: PASSED")


def test_deterministic_values():
    """
    Test with hardcoded values to ensure the math perfectly matches
    the expected symmetric cross-entropy formula.
    """
    # 2 items in batch, 2 dimensions
    I_f = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    T_f = torch.tensor([[1.0, 1.0], [0.0, 1.0]])
    t = torch.tensor(0.0)  # exp(0) = 1 (no temperature scaling)

    # I_e = [[1, 0], [0, 1]]
    # T_e = [[0.707, 0.707], [0, 1]]
    # Logits = I_e @ T_e.T = [[0.707, 0], [0.707, 1]]

    loss = clip_symmetric_loss(I_f, T_f, t)

    # Manual cross entropy calculation
    # Image-to-Text (axis 0):
    # Row 0: [-ln(e^0.707 / (e^0.707 + e^0))] = 0.4032
    # Row 1: [-ln(e^1 / (e^0.707 + e^1))] = 0.5514
    # loss_i = (0.4032 + 0.5514) / 2 = 0.4773

    # Text-to-Image (axis 1) uses transposed logits:
    # Col 0: [-ln(e^0.707 / (e^0.707 + e^0.707))] = 0.6931
    # Col 1: [-ln(e^1 / (e^0 + e^1))] = 0.3132
    # loss_t = (0.6931 + 0.3132) / 2 = 0.5032

    # Total loss = (0.4773 + 0.5032) / 2 = 0.4902

    expected_loss = 0.4902
    assert torch.isclose(
        loss, torch.tensor(expected_loss), atol=1e-3
    ), f"Expected {expected_loss}, got {loss.item()}"
    print("test_deterministic_values: PASSED")


# ==========================================
# Run all tests
# ==========================================
if __name__ == "__main__":
    test_output_shape_and_type()
    test_perfect_alignment()
    test_orthogonal_features()
    test_deterministic_values()
    print("All tests passed successfully! 🚀")
