import torch

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps" if torch.mps.is_available() else "cpu"
)


def test_torch(arr: torch.Tensor) -> float:
    """

    Args:
        arr:

    Returns: sum
    >>> test_torch([1, 2, 3])
    6.0
    """

    return float((torch.tensor(arr).to(device)).sum())
