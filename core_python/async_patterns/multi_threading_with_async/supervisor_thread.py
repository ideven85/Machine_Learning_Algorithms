from threading import Event, Thread

from core_python.async_patterns.multi_threading_with_async.blocking_code_display import (
    display_spinner,
    slow,
)


def supervisor():
    done = Event()
    to_console = Thread(target=display_spinner, args=("Thinking!", done))
    # print(f"Spinner Object: {to_console}")
    to_console.start()
    result = slow()
    done.set()
    to_console.join()
    return result


def main():
    result = supervisor()
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()
