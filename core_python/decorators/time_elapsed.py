import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args):
            start = time.perf_counter()
            _result = func(*args)
            elapsed = time.perf_counter() - start
            name = func.__name__
            args = ",".join(repr(arg) for arg in args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate