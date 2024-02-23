import math


def quadratic(a, b, c):
    delta = (b ** 2 - 4 * a * c)/(2*a)
    if delta<0:
        delta = (b**2+4*a*c)/(2*a)
    solution1 = (-b + (delta**0.5))