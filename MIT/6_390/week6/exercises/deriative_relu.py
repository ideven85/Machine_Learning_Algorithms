import numpy as np


def relu(x):
    """
    returns max of 0 and x
    """
    return np.maximum(0, x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


def gelu(x, phi):
    return phi * x


def derivative_relu(x):
    return np.where(x > 0, 1, 0)
