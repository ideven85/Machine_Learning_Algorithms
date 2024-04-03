from time import time


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def main():
    start = time()
    print(list(factorial(i) for i in range(100)))
    print("Time: ", time() - start)

    print("Hello, This is my first file")


if __name__ == "__main__":
    main()
