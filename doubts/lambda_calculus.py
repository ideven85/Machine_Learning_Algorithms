import time


def apply_n_times(f, n, x):
    out = x
    for _ in range(n):
        out = f(out)
        print(out, end=" ")
    return out


print(apply_n_times(lambda x: x * x, 3, 4))

import matplotlib.pyplot as plt
import math


def sine_curve(lo, hi, step):
    xs = []
    ys = []
    curr = lo
    while curr <= hi:
        xs.append(curr)
        ys.append(math.sin(curr))
        curr += step
    plt.plot(xs, ys)
    plt.show()


sine_curve(-5, 5, 0.1)


def response(f, lo, hi, step):
    xs = []
    ys = []
    curr = lo
    while curr <= hi:
        xs.append(curr)
        ys.append(f(curr))
        curr += step
    # plt.legend("Curves")
    plt.plot(xs, ys)
    plt.show()


response(math.cos, -5, 5, 0.1)
response(lambda x: x**3, 0, 5, 0.001)
response(math.sin, -5, 5, 0.1)
response(math.sin, 0, 10, 0.01)
start = time.time() * 1_000_000_000
functions = []
for i in range(5):

    def func(x):
        yield x + i

    functions.append(func)
for f in functions:
    print(list(f(12)))
second = time.time() * 1_000_000_000
functions1 = []
for i in range(5):

    def func(x):
        return x + i

    functions1.append(func)
for f in functions1:
    print(f(12))
third = time.time() * 1_000_000_000
print("First took", second - start)
print("Second took", third - second)
squares = lambda x: x * x
filter_odd = lambda x: x % 2 != 0  # boolean Function
# filter_odd_squared = lambda x:filter_odd(squares(x))
L = list(range(10))
# f=filter_odd_squared(10)
# print(f)
f1 = [squares(x) for x in L if filter_odd(x)]
print(f1)
out = [x * 2 for x in f1]
L2 = list(range(0, 20, 2))
zipped = [x - y for x, y in zip(L, L2)]
print(zipped)
