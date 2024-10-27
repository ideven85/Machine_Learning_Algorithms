import time


def fib(n):
    cache = {}

    def _fib(n):
        if n not in cache:
            if n < 2:
                cache[n] = n
            else:
                cache[n] = _fib(n - 1) + _fib(n - 2)
        return cache[n]

    return _fib(n)


start = time.perf_counter()
print(fib(100))
end = time.perf_counter()
print(end - start)

cache = {}


def fib1(n):
    if n not in cache:
        if n < 2:
            cache[n] = n
        else:
            cache[n] = fib1(n - 1) + fib1(n - 2)
    return cache[n]


start = time.perf_counter()
print(fib1(100))
end = time.perf_counter()
print(end - start)
