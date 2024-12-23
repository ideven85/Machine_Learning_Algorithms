"""
Question 3: Fill in the missing code below for the
following Vector class methods.

You may test your code by running
the doctests provided. Note that many doctests rely on a correct __repr__
implementation.
"""

import doctest
import math


class Vector:
    """
    Nd Vector object; has immutable tuple of coords
    """

    def __init__(self, coords):
        """
        >>> v = Vector([2, 3])
        >>> v.coords == (2, 3)
        True
        """
        self.coords = tuple(coords)

    def __repr__(self):
        """
        >>> v = Vector([0, -4])
        >>> repr(v)
        'Vector((0, -4))'
        """
        return f"Vector({self.coords})"

    def __add__(self, other):
        """
        >>> Vector([1, 2]) + Vector([1, 0])
        Vector((2, 2))
        """
        x = list(self.coords)
        x = [a + b for a, b in zip(x, list(other.coords))]
        self.coords = tuple(x)
        return self

    def __sub__(self, other):
        """
        >>> Vector([1, 2]) - Vector([1, 0])
        Vector((0, 2))
        """
        x = list(self.coords)
        x = [a - b for a, b in zip(x, list(other.coords))]
        self.coords = tuple(x)
        return self

    def __mul__(self, other):
        """
        >>> Vector([1, 2]) * 5
        Vector((5, 10))
        """
        x = list(self.coords)
        x = [n * other for n in x]
        self.coords = tuple(x)
        return self

    def __truediv__(self, other):
        """
        >>> Vector([4, 2]) / 2
        Vector((2.0, 1.0))
        """
        x = list(self.coords)
        x = [n / other for n in x]
        self.coords = tuple(x)
        return self

    def __abs__(self):
        """
        >>> abs(Vector([3, 4]))
        5.0
        """
        total = 0
        for x in self.coords:
            total += x**2
        return math.sqrt(total)

    def normalize(self):
        """
        >>> v = Vector([3, 4]).normalize()
        >>> abs(.6 - v.coords[0]) <= 1e-4 and abs(.8 - v.coords[1]) <= 1e-4
        True
        """
        x = list(self.coords)
        x = [n / abs(self) for n in x]
        self.coords = tuple(x)
        return self


if __name__ == "__main__":
    doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=doctest_flags)

    # doctest.run_docstring_examples(
    #    Vector.normalize,
    #    globals(),
    #    optionflags=doctest_flags,
    #    verbose=False
    # )
