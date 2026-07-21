# 6.101 recitation: linked lists


# Python list vs. linked-list
lst1 = [1, 2, 3]
ll1 = (1, (2, (3, None)))

lst2 = [3]
ll2 = (3, None)

lst3 = []
ll3 = None


def first(ll):
    """
    returns the first element of a non-empty linked list

    >>> first((5, (10, (15, None))))
    5
    """
    pass


def rest(ll):
    """
    returns the rest of a nonempty linked list (omitting the first element)

    >>> rest((5, (10, (15, None))))
    (10, (15, None))
    """
    pass


def ll_len(ll):
    """
    get the length of a linked list

    >>> ll_len(('a',('b',None)))
    2
    """
    pass


def ll_get(ll, ix):
    """
    get the ith element of a linked list

    >>> ll_get(('a',('b',None)), 1)
    'b'
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
