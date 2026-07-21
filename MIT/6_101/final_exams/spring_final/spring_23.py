# Time 3 hours Start Time 11:20 PM
# Q1
def swap_pairs(inp):
    """
    >>> swap_pairs([])
    []
    >>> swap_pairs([1])
    [1]
    >>> swap_pairs([1, 2])
    [2, 1]
    >>> swap_pairs([1, 2, 3])
    [2, 1, 3]
    >>> swap_pairs([1, 2, 3, 4])
    [2, 1, 4, 3]
    """
    if len(inp) < 2:
        return inp[:]

    return [inp[1], inp[0]] + swap_pairs(inp[2:])


# Q2
class DefaultDict(dict):
    """

        We would like to implement a dictionary-like DefaultDict class that is a subclass of the built-in dict class.
    Instances of the DefaultDict class act like a normal dictionary except that when we call __getitem__ on a
    missing key, we would like to insert the key with a default value instead of raising a KeyError, and return
    that value. The default value is created by a call to a default_factory function with no arguments that was
    provided during instance creation. For example:

    If a default_factory is not provided, its value should default to None. In that case, if the key is missing,
    __getitem__ should raise a KeyError exception with the key as the argument. If a value for default_factory
    is provided and calling it raises an exception, this exception is propagated unchanged. Note that instance
    creation only supports the optional argument default_factory (i.e., it does not take additional initialization
    arguments).
        >>> ee = DefaultDict()
        >>> ee[5]
        Traceback (most recent call last):
        ...
        KeyError: 5
        >>> dd = DefaultDict(lambda : "my default")
        >>> dd[5]
        'my default'
        >>> dd
        {5: 'my default'}
        >>> dd[5] = 99
        >>> dd.get(7, "is a lucky number")
        'is a lucky number'
        >>> dd
        {5: 99}
        >>> dd[7]
        'my default'
        >>> dd
        {5: 99, 7: 'my default'}
        >>> ss = DefaultDict(list)
        >>> ss['first'].append(8)
        >>> ss
        {'first': [8]}
        >>> s = 'mississippi'
        >>> d = DefaultDict(int)
        >>> for k in s: d[k] += 1
        >>> sorted(d.items())
        [('i', 4), ('m', 1), ('p', 2), ('s', 4)]

    """

    def __init__(self, default_factory=None):
        super().__init__()

        self.default_factory = default_factory

    def __getitem__(self, key):
        if key not in self:
            if self.default_factory is None:
                raise KeyError(key)
            self[key] = self.default_factory()
        return super().__getitem__(key)


# Question 3a:
class Foo:
    """
     >>> a= Foo()
     >>> a.update(10)
    >>> a.foo
    11
    >>> Foo.foo
    1


    """

    foo = 1

    def update(self, i):
        self.foo = self.foo + i


# Question3b:
class A:
    """
    >>> a = A()
    >>> a.update(10)
    >>> a.foo
    11
    >>> A.foo
    1
    """

    foo = 1

    def update(self, i):
        self.foo += i


class B:
    """
    >>> a = B()
    >>> a.update(10)
    >>> a.foo
    [1, 10]
    >>> B.foo
    [1]
    """

    foo = [1]

    def update(self, i):
        self.foo = self.foo + [i]


class C:
    """
    >>> a = C()
    >>> a.update(10)
    >>> a.foo
    [1, 10]
    >>> C.foo
    [1, 10]
    """

    foo = [1]

    def update(self, i):
        self.foo += [i]  # Extending in place


# Question 4
def combos(inp):
    """
        Given a list of elements, write a function that returns a list of lists, consisting of all of the possible combinations
    of the elements of the original list. Elements in the original list can be assumed to be unique (i.e., appear in
    the list only once). Note that the order of the elements in each combination, and the order of combinations in
    the output list, do not matter.
    >>> sorted(combos([1, 2]))
    [[], [1], [1, 2], [2]]
    >>> sorted(combos([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    if not inp:
        return [[]]
    clist = []
    # for el in inp:
    #     for i in range(len(clist)):
    #         temp = clist[i]
    #         clist.append(temp+[el])
    # return clist
    for combo in combos(inp[1:]):
        clist.append(combo)
        clist.append(inp[0:1] + combo)
    return clist


# Question 4b:
def combos_gen(inp):
    """
        Given a list of elements, write a function that returns a list of lists, consisting of all of the possible combinations
    of the elements of the original list. Elements in the original list can be assumed to be unique (i.e., appear in
    the list only once). Note that the order of the elements in each combination, and the order of combinations in
    the output list, do not matter.
    >>> sorted(combos_gen([1, 2]))
    [[], [1], [1, 2], [2]]
    >>> sorted(combos_gen([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    if not inp:
        yield []
        return
    for combinations in combos_gen(inp[1:]):
        yield inp[0:1] + combinations
        yield combinations
