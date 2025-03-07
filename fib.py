# fib.py

import os
import threading


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


# numpy_threads.py

import numpy as np

rng = np.random.default_rng()
matrix = rng.random(size=(50000, 50000))
matrix @ matrix
# for _ in range(os.cpu_count()):
#     threading.Thread(target=fib, args=(35,)).start()
