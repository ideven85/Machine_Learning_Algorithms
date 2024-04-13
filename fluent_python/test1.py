# import sys


def main():
    a = int(input("Please enter first:"))
    b = int(input("Please enter second:"))
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print("Cannot divide by zero", e)
    else:
        print("Else")
    finally:
        print("Go to hell")


if __name__ == "__main__":
    main()
