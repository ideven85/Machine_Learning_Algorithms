import asyncio
import torch

print(torch.__version__)


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


async def fib(n):

    return n if n < 2 else await fib(n - 1) + await fib(n - 2)


async def main():
    x = await fib(10)
    print(x)


if __name__ == "__main__":
    asyncio.run(main())
