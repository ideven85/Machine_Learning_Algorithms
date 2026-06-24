def fn(a, b, c, d):
    a = a * b + c

    return True if a % d == 0 and a >= b and a >= c else False


print(fn(2, 3, 4, 10))
