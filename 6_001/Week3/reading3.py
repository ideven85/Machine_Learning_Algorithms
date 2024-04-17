from typing import List


def substract_lists(list1: List, list2: List) -> List:
    """
    2 lists of equal length
    Return the difference between the elements of the two lists
    Zip Function creates a tuple
    """
    assert len(list1) == len(list2)
    return [(x - y) for x, y in zip(list1, list2)]

def first_occurrence(data):
    """
    Given a list of integers or strings, return a new list with the same
    set of items in the same order, but keeping only the first occurrence of
    each item.
    >>>first_occurrence([1, 9, 1, 1, 5, 3, 2, 9, 10]) == [1, 9, 5, 3, 2, 10]
    True
    """
    visited = set()
    out = []
    for val in data:
        if val in visited:
            continue
        else:
            out.append(val)
            visited.add(val)
    return out

import doctest
if __name__ == "__main__":
    print(doctest.testmod(verbose=True))
    a = [1]
    b = [2]
    d = [3, 4]
    c = zip(a, b, d)
    # print(list(c))
    print(*c)
    x = list(range(-10, 10))
    print({-val for val in x if val < 0})
