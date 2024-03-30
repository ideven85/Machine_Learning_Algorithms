x = 0


def foo(x):
    def bar():
        print("bar", x)

    bar()
    print("foo", x)


foo(1)
print("foo", x)
