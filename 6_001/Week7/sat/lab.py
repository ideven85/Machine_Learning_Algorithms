"""
6.101 Lab:
SAT Solver
"""

#!/usr/bin/env python3

import sys
import typing
# 10 hours per lab
"""
Back Tracking Satisfiability Solver
"""
sys.setrecursionlimit(10_000)
# NO ADDITIONAL IMPORTS


def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])
    The return value of satisfying_assignment is a dictionary mapping variables to the Boolean values that have been inferred for them (or None if no valid mapping exists).

So, we can see that, in our example above, Tim the Beaver is guilty and has a taste for vanilla and pickles!

It turns out that there are other possible answers that have Tim enjoying other flavors, but it also turns out that Tim is the uniquely determined culprit. How do we know? The SAT solver fails to find an assignment when we add an additional rule proclaiming Tim's innocence.
    """
    return True


def boolify_scheduling_problem(student_preferences, room_capacities):
    """
    Convert a quiz-room-scheduling problem into a Boolean formula.

    student_preferences: a dictionary mapping a student name (string) to a set
                         of room names (strings) that work for that student

    room_capacities: a dictionary mapping each room name to a positive integer
                     for how many students can fit in that room

    Returns: a CNF formula encoding the scheduling problem, as per the
             lab write-up
    
    We assume no student or room names contain underscores.
    """
    raise NotImplementedError


if __name__ == "__main__":
    import doctest
    rules={'saman': False, 'jonathan': False, 'chocolate': False, 'adam': False,
 'duane': False, 'pickles': True, 'tim': True, 'vanilla': True}

    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags)
