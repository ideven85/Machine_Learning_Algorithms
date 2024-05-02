"""
Question 2: Fill in the missing code below for the
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

    def add(self, other):
        """
        >>> Vector([1, 2]).add(Vector([1, 0]))
        Vector((2, 2))
        """
        x = list(self.coords)
        x = [a + b for a, b in zip(x, list(other.coords))]
        self.coords = tuple(x)
        return self

    def sub(self, other):
        """
        >>> Vector([1, 2]).sub(Vector([1, 0]))
        Vector((0, 2))
        """
        x = list(self.coords)  # Repeated Code
        x = [a - b for a, b in zip(x, list(other.coords))]
        self.coords = tuple(x)
        return self

    def scale(self, other):
        """
        >>> Vector([1, 2]).scale(5)
        Vector((5, 10))
        """
        x = list(self.coords)
        x = [n * other for n in x]
        self.coords = tuple(x)
        return self

    def div(self, other):
        """
        >>> Vector([4, 2]).div(2)
        Vector((2.0, 1.0))
        """
        if other == 0:
            return self
        x = list(self.coords)
        x = [n / other for n in x]
        self.coords = tuple(x)
        return self

    def magnitude(self):
        """
        >>> Vector([3, 4]).magnitude()
        5.0
        """
        total = 0
        a = list(self.coords)
        a = math.sqrt(sum([x * x for x in a]))
        return a

    def normalize(self):  # Creates a unit vector in the same direction
        """
        >>> v = Vector([3, 4]).normalize()
        >>> abs(.6 - v.coords[0]) <= 1e-4 and abs(.8 - v.coords[1]) <= 1e-4
        True
        """

        x = list(self.coords)
        magnitude = 0
        for i in range(len(x)):
            magnitude = x[i] * x[i]
        magnitude = math.sqrt(magnitude)
        if not magnitude:
            return self

        x = [n / self.magnitude() for n in x]
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
