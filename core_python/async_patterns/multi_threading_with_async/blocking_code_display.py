import itertools
import time
from threading import Event


def display_spinner(message: str, done: Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {message}"
        print(status, end="", flush=True)
        if done.wait(0.1):  # Apparently No interrupted  exception here
            break

        blanks = " " * len(status)
        print(f"\r{blanks}\r", end="")


def slow():
    time.sleep(3)  # No need to throw exception again
    return 42
