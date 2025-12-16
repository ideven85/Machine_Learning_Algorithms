# 6.101 recitation: LISP part 2, control structures


def abs(x):
    if x < 0:
        return -x
    return x


def sum_squares(n):
    total = 0
    for i in range(n + 1):
        total += i * i
    return total


#### heron's method for square roots


def sqrt(x, epsilon):
    guess = x / 2
    while abs(guess**2 - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess


out = sqrt(20, 1e-3)
print(out)
print(out**2)
