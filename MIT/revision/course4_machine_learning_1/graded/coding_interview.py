"""
Given a list as input, your task is to check if the list is strictly increasing. i.e. the numbers in the list should be in an increasing order. Hence, a number at a lower index should always be smaller than a number at a higher index.
Assume that the list will only have positive integers.
Print "yes" if the list is in strictly increasing order and print "no" if the list is not strictly increasing.

"""

import ast, sys


def is_increasing(lst):

    for i in range(len(lst) - 1):
        if lst[i + 1] <= lst[i]:
            print("no")
            return
    print("yes")


def main():
    input_str = sys.stdin.read()
    input_list = ast.literal_eval(input_str)

    l = [1, 4, 300, 400, 400]
    is_increasing(input_list)


if __name__ == "__main__":
    main()
