from sympy import *

x, y = symbols("x y")
expr = 2 * x + y
a = diff(sin(x) * exp(x), x)
print(a)
print(repr(a))
