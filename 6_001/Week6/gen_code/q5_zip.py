"""
Question 5: Implement the my_zip function as a generator

You may test this functions by running `pytest q5_zip.py` (no quotes)
in the terminal.
"""

def my_zip(x, y):
    pass

def test_my_zip():
    import types
    # erase zip
    global zip
    f = zip
    zip = None

    x = range(0, 4)
    y = "ABCD"
    z = [2, 4, 6]
    x1, x2 = f(x, y), my_zip(x, y)
    assert isinstance(x2, types.GeneratorType), f'my_zip should produce a generator!'
    assert list(x1) == list(x2)
    # check that the generator is exhausted
    assert list(x1) == list(x2)


    assert list(f(y, z)) == list(my_zip(y, z))
    assert list(f(f(y, z), x)) == list(my_zip(my_zip(y, z), x))





