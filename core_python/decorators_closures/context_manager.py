# Context Manager... use? No idea right now
class Manager:
    def __init__(self):
        print("Started Manager")

    def __enter__(self):
        print("Enter block")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exit block")


def main():
    #try 1
    Manager()
    print("Outside the context manager")
    with Manager() as manager:
        print("Inside the context manager")


if __name__ == '__main__':
    main()