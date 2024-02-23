"""
Not a clue what is in this file
"""


import operator
from multiprocessing import freeze_support
from multiprocessing.managers import BaseProxy, BaseManager


class Foo:
    def f(self):
        print("You called Foo.f()")

    def g(self):
        print("You called Foo.g()")

    def _h(self):
        print("You called Foo._h()")


def squares():
    for i in range(10):
        yield i*i


class GeneratorProxy(BaseProxy):
    _exposed_ = ['__next__']

    def __iter__(self):
        return self

    def __next__(self):
        return self._callmethod('__next__')

def get_operator_module():
    return operator

class MyManager(BaseManager):
    pass

MyManager.register('Foo1',Foo)
MyManager.register('Foo2',Foo,exposed=('g','_h'))
MyManager.register('baz',squares,proxytype=GeneratorProxy)

MyManager.register('operator',get_operator_module)

def test():
    manager = MyManager()
    manager.start()

    fn = manager.Foo1()
    #print(fn.__doc__)
    fn.f()
    fn.g()

    assert not  hasattr(fn,'_h')

    op = manager.operator()
    print('op.add(23, 45) =', op.add(23, 45))
    print('op.pow(2, 94) =', op.pow(2, 94))
    print('op._exposed_ =', op._exposed_)

if __name__ == '__main__':
    freeze_support()
    test()




