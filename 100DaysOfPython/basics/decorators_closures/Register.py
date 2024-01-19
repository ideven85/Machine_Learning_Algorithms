registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def foo1():
    print("foo1 Function")


@register
def foo2():
    print("foo2 Function")




def foo3():
    print("foo3 Function")

if __name__ == '__main__':
    print("Inside Main")
    print("Registry",registry)
    """
    Made a call to registry list calling foo1 function
    """
    print(registry[0])
    print(registry[1])

    foo1()
    foo2()
    foo3()
    # for e in registry: e()