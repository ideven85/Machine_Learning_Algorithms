import asyncio


def simplest_coroutine():
    print("Starts:")
    x = yield
    print("Simplest Coroutine received:", x)


async def f(x):
    r = await g(x)
    return r


async def g(x):
    return x


"""
Generating async fib
"""
# async def fib(n):
#     if n<2:
#         return n
#     return await(fib(n-1))+await(fib(n-2))


async def main():
    #  # Not when coroutine is started I think
    return await f([1, 2, 3])
    # return fib(100)


if __name__ == "__main__":
    # a = simplest_coroutine()
    # print(next(a))
    print(asyncio.run(main()))
