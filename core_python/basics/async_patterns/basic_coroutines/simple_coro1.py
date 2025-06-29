def simplest_coroutine():
    print("Starts:")
    x = yield
    y = yield
    print("Simplest Coroutine received:", x)


def f():
    yield from simplest_coroutine()


def simple_coro2(val):
    print("Starts", val)
    x = yield val
    print("Received x:", x)
    y = yield x + val
    print("Received y:", y)


def main():
    f = simple_coro2(42)
    while f.__next__():
        if f.__next__():
            print(next(f))
    f1 = f

    # f.send(100)
    # print(next(f))


if __name__ == "__main__":
    main()
    # x=simplest_coroutine()

    # print(next(simplest_coroutine()))
    # print(next(simplest_coroutine()))
    # print(next(x))
    # print(x.send(None))
    # y=f()
    # print(next(y))
    # print(next(y))

    # print(next(f))
    # print(next(f))
