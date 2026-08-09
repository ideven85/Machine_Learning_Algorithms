def hello():
    print("Hello")


def fib(n):
    """
    >>> list(clocked_algos(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


    """
    a = 0
    b = 1
    c = 0
    for _ in range(n + 1):
        yield a

        # b = a + b
        a, b = b, a + b


def test_hello():
    assert "Hello"


def test_fib():
    pass
