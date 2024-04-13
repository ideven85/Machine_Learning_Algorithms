import os
import pickle

TEST_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data")

import poly
# run `pytest test_poly.py` (no quotes)
# in your terminal to see the test results!

def test_add_tiny():
    """
    Test case checking that poly_add can add
    x^2 + 3x  to  4x^3 + 7x - 8  and get 4x^3 + x^2 + 10x - 8
    """
    assert False, "Implement me!"


def test_add_small():
    with open(os.path.join(TEST_DIR, "add_tests.pickle"), "rb") as f:
        for p1, p2, out in pickle.load(f):
            assert poly.poly_add(p1, p2) == out


def test_mul_tiny():
    """
    Test case checking that poly_mul can multiply
    6x^7 + 2x^4 + 5x^3 by 4x^2 + 3x
    and get
    24x^9 + 18x^8 + 8x^6 + 26x^5 + 15x^4
    """
    p1 = [0, 0, 0, 5, 2, 0, 0, 6]
    p2 = [0, 3, 4]
    p1_copy = p1.copy()
    p2_copy = p2.copy()
    exp = [0, 0, 0, 0, 15, 26, 8, 0, 18, 24]
    assert poly.poly_mul(p1, p2) == exp
    assert p1 == p1_copy and p2 == p2_copy
    assert poly.poly_mul(p2, p1) == exp
    assert p1 == p1_copy and p2 == p2_copy


def test_regular_mul():
    with open(os.path.join(TEST_DIR, "multiply_tests.pickle"), "rb") as f:
        for p1, p2, out in pickle.load(f):
            assert poly.poly_mul(p1, p2) == out


def test_sparse_mul():
    with open(os.path.join(TEST_DIR, "sparse_multiply_tests.pickle"), "rb") as f:
        for p1, p2, out in pickle.load(f):
            assert poly.poly_mul(p1, p2) == out

def test_subtract_tiny():
    """
    Test case checking that poly_subtract can subtract
    x^2 + 3x  from  4x^3 + 7x - 8  and get 4x^3 - x^2 + 4x - 8
    """
    p1 = [0, 3, 1]
    p2 = [-8, 7, 0, 4]
    # check that we get expected result
    assert poly.poly_subtract(p1, p2) == [8, -4, 1, -4]
    # check that the inputs are unmodified
    assert p1 == [0, 3, 1] and p2 == [-8, 7, 0, 4]
    # reversing order should get a different result
    assert poly.poly_subtract(p2, p1) == [-8, 4, -1, 4]
