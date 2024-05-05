# pylint: disable=invalid-name
test_list = """
       >>> f = [1, 1, 2, 3]
       >>> f += [f[-1] + f[-2]]
       >>> f == [1, 1, 2, 3, 5]
       True
"""


def factorial(n: int) -> int:
    """
    Compute n! recursively.
    :param n: an integer >= 0
    :returns: n!
    Because of Python's stack limitation, this won't compute a value larger than about 1000!.
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest

    __test__ = {name: value for name, value in locals().items()}
    print(__test__)
    doctest.testmod(verbose=True)
