import asyncio
import time


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


async def main():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    i = 20
    while loop.time() < end_time:
        print(factorial(i))
        await asyncio.sleep(1)
        i += 1


asyncio.run(main())
