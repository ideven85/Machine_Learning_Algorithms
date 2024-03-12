from typing import List


def substract_lists(list1:List, list2:List)->List:
    """
    2 lists of equal length
    Return the difference between the elements of the two lists
    Zip Function creates a tuple
    """
    assert len(list1) == len(list2)
    return [(x-y) for x, y in zip(list1, list2)]


if __name__ == '__main__':
    a = [1]
    b = [2]
    d=[3,4]
    c = zip(a,b,d)
    print(type(c))
    print(*c)
    x=list(range(-10,10))
    print([-val for val in x if val<0])