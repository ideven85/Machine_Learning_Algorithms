"""
Question 2: Fill in the missing code below for the
following Vector class methods.

You may test your code by running
the doctests provided. Note that many doctests rely on a correct __repr__
implementation.
"""

import doctest

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
        pass

    def __repr__(self):
        """
        >>> v = Vector([0, -4])
        >>> repr(v)
        'Vector((0, -4))'
        """
        pass

    def add(self, other):
        """
        >>> Vector([1, 2]).add(Vector([1, 0]))
        Vector((2, 2))
        """
        pass

    def sub(self, other):
        """
        >>> Vector([1, 2]).sub(Vector([1, 0]))
        Vector((0, 2))
        """
        pass

    def scale(self, other):
        """
        >>> Vector([1, 2]).scale(5)
        Vector((5, 10))
        """
        pass

    def div(self, other):
        """
        >>> Vector([4, 2]).div(2)
        Vector((2.0, 1.0))
        """
        pass

    def magnitude(self):
        """
        >>> Vector([3, 4]).magnitude()
        5.0
        """
        pass

    def normalize(self):
        """
        >>> v = Vector([3, 4]).normalize()
        >>> abs(.6 - v.coords[0]) <= 1e-4 and abs(.8 - v.coords[1]) <= 1e-4
        True
        """
        pass




if __name__ == "__main__":
    doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=doctest_flags)


    # doctest.run_docstring_examples(
    #    Vector.normalize,
    #    globals(),
    #    optionflags=doctest_flags,
    #    verbose=False
    # )