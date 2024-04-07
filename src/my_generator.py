def fib(n):
    if n == 0:
        yield n
    elif n == 1:
        yield n
    else:
        x = 0
        y = 1
        for i in range(1, n + 1):
            y = y + x
            x = y - x
            yield y


a = fib(10)
print(list(a))
