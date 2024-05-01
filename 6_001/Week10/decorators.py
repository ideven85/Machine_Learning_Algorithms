def memoise(func):
    cache = {}

    def _mfunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return _mfunc


@memoise
def fib(n):
    if n < 2:
        return n
    print(n, end=" ")
    return fib(n - 1) + fib(n - 2)


def fib1(n):
    if n < 2:
        return n
    print(n, end=" ")
    return fib1(n - 1) + fib1(n - 2)


f = memoise(fib1)
print(fib(20))

print(f(20))
