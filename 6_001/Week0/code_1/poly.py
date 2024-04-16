"""
Note that there are many ways to represent polynomials in Python.
Today we will represent polynomials are represented as lists,
where the index represents the power and the element represents
the coefficient value.

Ex: 3x^3 + x + 2 would be represented as [2, 1, 0, 3]

Write code in the functions below to perform operations
on any two polynomials in list form, p1 and p2.
"""


def poly_add(p1, p2):
    """
    Takes two single variable polynomials as input and returns a
    new polynomial representing their sum. Does not modify inputs.
    """
    out = p1.copy()
    for i in range(len(p1)):
        out[i] += p2[i]
    return out


def poly_mul(p1, p2):
    """
    Takes two single variable polynomials as input and returns a
    new polynomial representing their product. Does not modify inputs.
    """
    raise NotImplementedError


def poly_subtract(p1, p2):
    """
    Takes two single variable polynomials as input and returns a
    new polynomial representing their p1 - p2. Does not modify inputs.
    """
    raise NotImplementedError
