class DefaultDict(dict):
    """
    >>> dd = DefaultDict(lambda : 'my default')
    >>> dd[5]
    'my default'
    >>> dd
    {5: 'my default'}
    >>> dd[5] = 99
    >>> dd.get(7, 'is a lucky number')
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
    >>> for k in s:     d[k] += 1
    >>> sorted(d.items())
    [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
    >>> ee = DefaultDict()
    >>> ee[5]
    Traceback (most recent call last):
        ...
        KeyError: 5
    """

    def __init__(self, default_factory=None):
        super().__init__()
        self.default_factory = default_factory

    def __getitem__(self, key):
        if key not in self:
            if not self.default_factory:
                raise KeyError(key)
            self[key] = self.default_factory()
        return super().__getitem__(key)


import doctest

doctest.testmod(verbose=True)
