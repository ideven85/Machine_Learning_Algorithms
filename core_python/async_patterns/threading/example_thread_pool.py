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
    start = time.perf_counter_ns()
    for result in pool.map(factorial, range(2, 100)):
        print(f"Got {result}")
    end = time.perf_counter_ns()
    print(end - start)
