x = 100


def outer():
    global x
    x += 1

    def inner():
        # What if we
        global x
        x += 2  # What if I want this to point to outer function's x?

        print("Inner function", x)

    inner()
    """
    So it's useful to think about that inner function object not only as an object unto itself but as the combination of the function
     and the frame where it was created (its "enclosing environment") as a single entity,
     which we've circled in green here. Why? 
     Because the function has access to all of these variables defined in the parent frame.
      That entity is what we refer to as a closure -- the combination of a function object and its enclosing environment.
    """
    print("Outer function", x)


def add_n(n):

    def inner(x):
        return x + n

    return inner


def square(x):
    return x * x


cube = lambda x: x**3


def make_adder(n):
    return lambda x: x + n


functions = []
for i in range(5):
    functions.append(make_adder(i))  # 12,13 because n is bound to make adder


def make_adder1():
    return lambda x: x + 1


f1 = []
for i in range(5):

    f1.append(make_adder1())


if __name__ == "__main__":
    print("Global", x)
    outer()
    # inner()
    print("Global", x)
    add1 = add_n(1)
    add2 = add_n(2)
    print(add1(9))
    print(add2(8))
    print(add_n(4)(6))
    print(square)

    for f in functions:
        print(f(12))
    for f in f1:
        print(f(12), end=" ")

    print()
    print(add1.__closure__[0].cell_contents)
