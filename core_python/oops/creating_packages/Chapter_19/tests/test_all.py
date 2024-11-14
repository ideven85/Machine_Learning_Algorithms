# A Test Module
# ----------------

"""Test all features of some_algorithm.

Requires some_algorithm package be on the PYTHONPATH.
"""

# Imports

import unittest
from ..some_algorithm import *

# Test Case


class TestSomeAlgorithm(unittest.TestCase):

    def test_import_should_see_value(self):
        x = SomeAlgorithm()
        x1 = SomeAlgorithm1()
        assert 2**42 == x.value()
        assert 42 == x1.value()


# Run the implicit test suite if this is used as a main program.

if __name__ == "__main__":
    unittest.main(exit=False)
