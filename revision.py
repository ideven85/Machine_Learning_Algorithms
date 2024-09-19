import numpy as np


def memoised_wrapper(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


@memoised_wrapper
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def main():
    l = np.arange(10)
    print([fib(i) for i in l])



if __name__ == "__main__":
    main()
