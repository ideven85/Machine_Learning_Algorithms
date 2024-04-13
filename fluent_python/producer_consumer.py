import asyncio


async def main():
    await asyncio.sleep(1)
    print("hello")

# function to add two numnbers
def add(a, b):
    return a + b

# function to test add add
def test_add1(a,b):
    
def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2
    assert add(-3, -5) == -8

# function to multiply two numbers
def mul(a,b):
    return a*b


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(...))
        task2 = tg.create_task(another_coro(...))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")


with asyncio.Runner() as runner:
    runner.run(main())
