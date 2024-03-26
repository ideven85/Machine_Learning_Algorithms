import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 201)
fig, ax = plt.subplots(2)
ax[0] = plt.plot(x, np.sin(x))
ax[1] = plt.plot(x, np.cos(x))

fig.tight_layout()

plt.show()
