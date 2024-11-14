import asyncio

"""
Important In this documentation the term “coroutine” can be used for two closely related concepts:
a coroutine function: an async def function;
a coroutine object: an object returned by calling a coroutine function.
"""


async def nested():  # Coroutine Function
    print("Hi")
    return 42


async def main():
    task = asyncio.create_task(nested())  # Coroutine Object
    # print(task.result())
    print(await task)
    # print(dir(task))


if __name__ == "__main__":
    asyncio.run(main())  # Returns Nothing
    # t=asyncio.sleep(10,result='Hi') # No idea still
