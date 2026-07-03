import numpy as np

x = np.array([1, 0])
mu = x.mean()
variance = x.var()
std_dev = np.sqrt(variance)
print(
    f"Mean: {mu}, Std Deviation: {std_dev}, Variance: {variance}, By np Std_dev: {np.std(x)}"
)
