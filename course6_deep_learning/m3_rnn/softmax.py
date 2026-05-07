import numpy as np


def softmax(x):
    """Softmax activation function"""
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / exp_x.sum(axis=1, keepdims=True)
