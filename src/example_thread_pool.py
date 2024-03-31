import time
from multiprocessing.pool import ThreadPool


def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


with ThreadPool() as pool:
    start = time.time()
    for result in pool.map(factorial,range(2,200)):
        print(f'Got {result}')
    end = time.time()
    print(end-start)
