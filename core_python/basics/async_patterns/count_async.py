import asyncio
import time


async def factorial(n):  # Coroutine Function
    # return 1 if n<2 else n*factorial(n-1) # What will be this?
    if n < 2:
        return 1
    else:
        # await n*factorial(n-1) # Ok object await
        # t=factorial_plain(10)
        return (
            await factorial(n - 1) * n
        )  # factorial(n-1) should come first coz it's an int object


async def count():
    print("First Count")
    await asyncio.sleep(1)
    print("Second Value")


def factorial_plain(n):
    return 1 if n < 2 else factorial_plain(n - 1) * n


async def main():
    #
    print(
        await asyncio.gather(
            factorial(10), factorial(20), factorial(30), factorial(100)
        )
    )
    await asyncio.gather(count(), count(), count())

    r = factorial(10)
    print("Plain:", factorial_plain(100))
    print("Coroutine:", await r)


if __name__ == "__main__":
    s1 = time.perf_counter()
    asyncio.run(main())  # awaits coroutine main how?
    s2 = time.perf_counter() - s1
    print(f"{__file__} ran in {s2:.8f} seconds")
