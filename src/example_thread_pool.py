import time
from multiprocessing.pool import ThreadPool


def factorial(n):
    i = 1
    if n < 2:
        return 1
    else:
        for j in range(2, n + 1):
            i = i * j
        return i


with ThreadPool() as pool:
    start = time.time()
    for result in pool.map(factorial, range(2, 1000)):
        print(f"Got {result}")
    end = time.time()
    print(end - start)
