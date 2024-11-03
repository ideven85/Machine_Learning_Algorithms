# 6.101 recitation: linked lists and generators

#
# review from last time: the basic linked-list operations
#


def first(ll):
    """
    returns the first element of a non-empty linked list

    >>> first((5, (10, (15, None))))
    5
    """
    return ll[0]


def rest(ll):
    """
    returns the rest of a nonempty linked list (omitting the first element)

    >>> rest((5, (10, (15, None))))
    (10, (15, None))
    """
    return ll[1]


def ll_len(ll):
    """
    get the length of a linked list

    >>> ll_len(('a',('b',None)))
    2
    """
    if ll is None:
        return 0
    return 1 + ll_len(rest(ll))


def ll_get(ll, ix):
    """
    get the ith element of a linked list

    >>> ll_get(('a',('b',None)), 1)
    'b'
    """
    if ix == 0:
        return first(ll)
    return ll_get(rest(ll), ix - 1)


######################################################


def make_ll(*elements):
    """
    given an arbitrary number of elements as arguments,
    make a linked-list of (first,rest) pairs

    >>> make_ll(1, 2, 3)
    (1, (2, (3, None)))
    """
    pass


def ll_reverse(ll):
    """
    return the reverse of a linked list

    >>> ll_reverse(make_ll(1,2,3))
    (3, (2, (1, None)))
    """
    pass


def ll_concat(ll1, ll2):
    """
    return the concatenation of two linked lists

    >>> ll_concat(make_ll(1), make_ll(2,3))
    (1, (2, (3, None)))
    """
    pass


def ll_elements(ll):
    """
    generator that yields the elements in a linked list, so that it can be used
    in an iterative for loop like `for elt in ll_elements(ll)`

    >>> for i in ll_elements(make_ll(1, 2, 3)):
    ...     print(i)
    1
    2
    3
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
