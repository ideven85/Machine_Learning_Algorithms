import math


class FactorIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration("Overflow")
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result


def factorial(n):
    if n < 2:
        yield n
        return
    else:
        result = 1
        for i in range(1, n):
            result *= i
            yield result


def main():
    iterator = FactorIter(10)
    for x in iterator:
        print(x)
    for f in factorial(10):
        print(f, end=" ")


if __name__ == "__main__":
    main()
