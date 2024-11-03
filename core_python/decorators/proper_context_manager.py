from contextlib import contextmanager

class Manager:
    def __init__(self):
        print("Init method")

    def __enter__(self):
        #print("Enter method")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit method")

    def __str__(self):
        return "Enter method"


@contextmanager
def context_manager():
    print("Init Method")
    yield "Enter Method"
    print("Exit method")

def main():
    with context_manager() as manager:
        print(manager)
        print("context manager")

    print("\n\nNo Difference:\n\n")

    with Manager() as manager:
        print(manager)
        print("custom manager")


if __name__ == '__main__':
    main()