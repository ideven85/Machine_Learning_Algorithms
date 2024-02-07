import asyncio
import turtle

async def first():
    await asyncio.sleep(2)
    print("First Completed")

async def second():
    await asyncio.sleep(1)
    print("Second Completed")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.gather(first(),second()))
finally:
    loop.close()

