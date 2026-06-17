from ....utilties import utils, clock_utils as c

# from utilties import utils as utils
# from utilties.clock_utils import clock_deco
import pytest
from math import factorial


@c.clock_deco
def solver(me):
    return 1 if me < 2 else me * solver(me - 1)


# print(solver(10))


def test_solver():
    assert list(range(solver(10))) == list(range(factorial(10)))


print(list(range(solver(10))))
