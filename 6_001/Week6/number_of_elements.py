import math


# Add two numbers together
def add(a, b):
    return a + b


# Subtract two numbers together
def subtract(a, b):
    return a - b


# Factorial function
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def sine(period):
    n = 0
    print(n)
    while True:

        yield round(math.sin(n * 2 * math.pi / period), 6)
        n = (n + 1) % period


# factorial of a number
def factorialV3(n):
    return 1 if n < 2 else n * factorialV3(n - 1)


def salesman():
    a = [1, 2, 3]
    print()


a = sine(2)
print(len(list(a)))
