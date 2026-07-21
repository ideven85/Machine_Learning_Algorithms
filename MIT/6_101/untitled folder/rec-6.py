# 6.101 recitation: LISP part 2, lists

#######################################
# LINKED LIST REPRESENTATION REMINDER #
#######################################

# Python Lists:

x = [1, 2, 3]


# Can represent a linked-list with length-2 tuples instead, e.g.:

x = (1, (2, (3, None)))

# None represents the empty linked list,
# everything else is (elt, rest), where rest is a linked list

# (1, (2, None)) is a linked list
# None is (technically) a linked list (and empty one)
# (1, 2) is _not_, since 2 is not


# In Scheme*, these look similar but slightly different:
#  (cons 1 (cons 2 (cons 3 ())))
#
#  or, (list 1 2 3) makes the same thing
#  once you've implemented it


# each of these things (Python lists, or linked lists) is an _abstraction_ for
# an ordered sequence of elements, so we can use any of them interchangeably if
# we provide the right interface!  (more on that in a while...)

# one of the things we've found useful so far when thinking about recursive
# operations on lists is a "first/rest" split.  we can define these on any
# types, so:


def first(L):  # < -- for a Python list
    return L[0]


def rest(L):  # < -- for a Python list
    return L[1:]


# now we can write our functions in terms of "first" and "rest" to make them
# work with either linked lists or Python lists (separation of concerns!)
# thinking in those terms is also nice for this kind of linked list, which,
# being a two-element tuple, has that natural separation built in
#
# (in Scheme, these are called "car" and "cdr" instead of "first" and "rest",
# so let's use those names moving forward)


def car(L):
    return L[0]


def cdr(L):
    return L[1:]


#############
# EXERCISES #
#############


# x is a Python list [n1, n2, n3]
def sum_list(x):
    out = 0
    for i in x:
        out += i
    return out


def sum_nested(x):
    out = 0
    for i in x:
        out += sum_nested(i) if isinstance(i, list) else i
    return out


def subtract_elts(l1, l2):
    return [i - j for i, j in zip(l1, l2)]


def max(x):
    best = None
    for i in x:
        if best is None or i > best:
            best = i
    return best
