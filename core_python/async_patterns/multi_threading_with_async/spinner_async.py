import asyncio


# from threading import Event, Thread
import itertools
import time


async def display_spinner(message: str)-> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {message}"
        print(status, end="", flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break


        blanks = " " * len(status)

        print(f"\r{blanks}\r", end="")


async def slow():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(display_spinner("thinking!"))
    print(f"Spinner Object: {spinner}")
    result = await slow()
    spinner.cancel()
    return result


async def main():
    result = await supervisor() # asyncio.run without async main or like this
    print(f'\nAnswer: {result}')



if __name__ == "__main__":
    asyncio.run(main())

