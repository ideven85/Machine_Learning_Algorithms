import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - t0) * 100000
        name = func.__name__

        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f"{k}={v!r}" for k, v in kwargs.items())
        arg_str = ", ".join(arg_lst)
        print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}")
        return result

    return clocked


DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"


def clock_parametrised(fmt=DEFAULT_FMT):
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


@clock_parametrised(fmt=DEFAULT_FMT)
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(10))
