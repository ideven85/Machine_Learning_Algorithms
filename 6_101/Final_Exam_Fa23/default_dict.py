class DefaultDict(dict):
    def __init__(self, default_factory=None):
        super().__init__()
        if not default_factory:
            self.dd = dict()
        else:
            self.dd = default_factory()

    def __contains__(self, item):
        return item in self.dd

    def __getitem__(self, key):
        if self.__contains__(key):
            return self.dd[key]
        else:
            return None

    def __setitem__(self, key, value):
        self.dd[key] = value


"""
>>> dd = DefaultDict(lambda 5: "my default")
>>> dd[5]
"my default"
>>> dd
{5: "my default"}
>>> dd[5] = 99
>>> dd.get(7, "is a lucky number")
"is a lucky number"
>>> dd
{5: 99}
>>> dd[7]
"my default"
>>> dd
{5: 99, 7: "my default"}
>>> ss = DefaultDict(list)
>>> ss[’first’].append(8)
>>> ss
{’first’: [8]}
>>> s = ’mississippi’
>>> d = DefaultDict(int)
>>> for k in s:
...     d[k] += 1
>>> sorted(d.items())
[(’i’, 4), (’m’, 1), (’p’, 2), (’s’, 4)]
>>> ee = DefaultDict()
>>> ee[5]
KeyError: 5
"""
import doctest

doctest.testmod(verbose=True)
