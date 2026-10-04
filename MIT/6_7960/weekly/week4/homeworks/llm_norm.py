import numpy as np

def muon_newton_schulz(G, steps=5):
    """
    Computes U * V^T from a gradient matrix G using Newton-Schulz iteration.
    Bypasses explicit SVD.
    """
    # 0. Ensure matrix is formatted with the smaller dimension as rows for speed
    # (Muon transposes internally if rows < cols, here we assume standard orientation)
    X = G.copy()

    # 1. Spectral normalization (X_0 = G / ||G||_2 approximate norm)
    # This prevents the iteration from exploding
    norm = np.linalg.norm(X, ord=2)
    if norm > 0:
        X = X / norm

    # 2. Newton-Schulz Iteration loop: X = 0.5 * X * (3I - X^T * X)
    for _ in range(steps):
        XtX = np.matmul(X.T, X)
        I = np.eye(XtX.shape[0])
        term = 3.0 * I - XtX
        X = 0.5 * np.matmul(X, term)

    return X

# --- Verification Test ---
np.random.seed(42)
grad = np.random.randn(4, 4)  # Mock 4x4 gradient matrix

# Method 1: Iterative Muon Way
muon_result = muon_newton_schulz(grad, steps=6)

# Method 2: Ground Truth Exact SVD (U * V^T)
U, S, Vt = np.linalg.svd(grad, full_matrices=False)
exact_svd_result = np.matmul(U, Vt)

print("Are the Muon and true U*V^T matrices identical?")
print(np.allclose(muon_result, exact_svd_result, atol=1e-5))
