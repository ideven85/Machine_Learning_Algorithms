from multiprocessing import Process, Event

# from threading import Event, Thread
from multiprocessing import synchronize
import itertools
import time


def display_spinner(message: str, done: synchronize.Event) -> None:
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


def supervisor():
    done = Event()
    to_console = Process(target=display_spinner, args=("Thinking!", done))
    print(f"Spinner Object: {to_console}")
    to_console.start()
    result = slow()
    done.set()
    to_console.join()
    return result


def main():
    result = supervisor()
    print(f"\nAnswer: {result}")


if __name__ == "__main__":
    main()
