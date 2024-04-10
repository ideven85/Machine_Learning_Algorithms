"""
Question 2: Rewrite poly_evaluate to be more pythonic.
For an extra challenge, try doing it with one line of code!
"""
import math


def poly_evaluate(coefficients, x):
    """
    Parameters:
        coefficients : list of floats
        x : float
    Returns:
        The value of the polynomial
    coefficients[0]x^0 + coeff[1]x^1+... coeff[n-1]x^(n-1)
    """

    return sum([a*(x**b) for (a,b) in zip(coefficients, range(len(coefficients)))])

print(poly_evaluate([7, 1, 3], 2)) # outputs 21  (7 + 1*x + 3x^2)
assert poly_evaluate([7, 1, 3], 2) == 21
