import asyncio


async def main():
    await asyncio.sleep(1)
    print("hello")


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(...))
        task2 = tg.create_task(another_coro(...))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")


with asyncio.Runner() as runner:
    runner.run(main())
