import math


def quadratic(a, b, c):
    delta = (b ** 2 - 4 * a * c)

    solution1 = (-b + (delta**0.5)*c)/(2*a)
    solution2 = (-b-(delta**0.5)*c)/(2*a)
    return solution1, solution2
