import math
import matplotlib.pyplot as plt

def sine_curve(low, high, step):
    xs=[]
    ys=[]
    current=low
    while current<=high:
        xs.append(current)
        ys.append(math.sin(current))
        current+=step
    plt.plot(xs, ys)

sine_curve(-5,5,.1)
plt.show()