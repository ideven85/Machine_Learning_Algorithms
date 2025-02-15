# A Test Module
# ----------------

"""Test all features of some_algorithm.

Requires some_algorithm package be on the PYTHONPATH.
"""

# Imports

import unittest
import some_algorithm

# Test Case


class TestSomeAlgorithm(unittest.TestCase):

    def test_import_should_see_value(self):
        x = some_algorithm.SomeAlgorithm()
        x1 = some_algorithm.SomeAlgorithm1()
        assert 2**42 == x.value()
        assert 42 == x1.value()


# Run the implicit test suite if this is used as a main program.

if __name__ == "__main__":
    unittest.main(exit=False)
