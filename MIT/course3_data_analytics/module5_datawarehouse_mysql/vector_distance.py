import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum([x**2 for x in a[0]]))
