def double(x):
    return double(x * x)


first = double


def double(y):
    return y + y


result = first(3)
print(result)
