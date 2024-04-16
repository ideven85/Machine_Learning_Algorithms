from collections import OrderedDict

from debug_recursion import show_recursive_structure


def can_log(x):
    """ "
    Checks whether the log entry is valid or not
    Pythonic Coding
    """
    if isinstance(x, (str, float, int, bool, complex)):
        return True
    elif isinstance(x, (list, tuple, set, frozenset)):
        return all(can_log(v) for v in x)

    elif isinstance(x, (dict, OrderedDict)):
        return all((can_log(k) and can_log(v)) for k, v in x.items())
    else:
        return False


def sum_list(x):
    """
    Compute the sum of list recursively
    >>> sum_list([1,2,3])
    6
    """
    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]
    return x[0] + sum_list(x[1:])


def sum_nested(x):
    """
    Sums a nested list
    Nice Code By MIT
    >>> sum_nested([[1,2],3,[4,5],[[[6]]]])
    21
    """
    if not x or len(x) == 0:
        return 0
    if type(x[0]) is list:
        return sum_nested(x[0]) + sum_nested(x[1:])
    else:
        return x[0] + sum_nested(x[1:])


@show_recursive_structure
def productSum(array, multiplier=1):
    # Write your code here.
    total = 0
    if not array:
        return 0

    elif type(array[0]) is list:
        return productSum(
            array[0], multiplier=multiplier + 1
        ) * multiplier + productSum(array[1:], multiplier=multiplier)
    else:
        return array[0] * multiplier + productSum(array[1:], multiplier=multiplier)


count = 0


@show_recursive_structure
def subsequences(seq):
    """
    Given a tuple or list or other iterable, returns a set of tuples
    consisting of all its subsequences.
    A subsequence is a sequence of elements from seq that are in the same
    order as in seq but not necessarily adjacent.
    >>> sorted(subsequences([4,2,3]))
    [(), (2,), (2, 3), (3,), (4,), (4, 2), (4, 2, 3), (4, 3)]
    """
    global count
    if not seq:
        count += 1
        return {()}
    first = seq[0]
    rest = seq[1:]
    count += 1
    rest_seq = subsequences(rest)
    # print(rest_seq)
    first_seq = {(first,) + sub_seq for sub_seq in rest_seq}
    # print(first_seq)
    return first_seq | rest_seq  # Union
    # answer = {subsequences(rest)| (first,)+sub_seq for sub_seq in subsequences(rest)}
    # answer= ({(first,) + subseq for subseq in subsequences(rest)} | {subseq for subseq in subsequences(rest)})
    # return answer


def powerset(array):

    c = 0
    subSets = [[]]
    if not array:
        c += 1
        return {()}

    for element in array:
        for i in range(len(subSets)):
            c += 1
            currentSubSet = subSets[i]
            subSets.append(currentSubSet + [element])
    print("Powerset Inversions: ", c)
    return subSets


def number_to_string(n, b):
    """
    Given an integer n and base b (where 2 <= b <= 10),
    returns n represented as a string in base-b notation,
    without any unnecessary leading zeroes.
    >>> number_to_string(-829, 10)
    '-829'
    >>> number_to_string(-5, 2)
    '-101'
    >>> number_to_string(0, 10)
    '0'
    """
    if n < 0:
        return "-" + number_to_string(-n, b)
    elif n == 0:
        return "0"
    elif n < b:
        return str(n)
    else:
        digits = "0123456789"
        return number_to_string(n // b, b) + digits[n % b]


import doctest


# todo 25th March,2024
def powerset_recursive(arr):
    if not arr:
        return [[]]
    # if len(arr)==1:
    #     return [arr]
    first = arr[0]
    rest = arr[1:]
    rest_sequence = powerset_recursive(rest)
    # print(first_sequence)
    first_sequence = [first] + [sub_seq for sub_seq in rest_sequence]
    # print(rest_sequence)
    return first_sequence + rest_sequence


def powerset_backtracking(arr):

    def dfs(output, current=list(), start=0):
        if len(current) >= 1:
            output.append(current[:])

        for index in range(start, len(arr)):
            current.append(arr[index])
            dfs(output, current, index + 1)
            current.remove(arr[index])

    output = [[]]
    dfs(output)
    return output


if __name__ == "__main__":

    # print(sum_list([]))
    # print(sum_list([1,2,3,4,5]))
    # a = [[[6]]]
    # print(type(a[0][0][0]))
    # print(type(a))
    # print(len(a))
    # #print(a[0]+1)
    # print(productSum([[1,2],3,[4,5],[[[6]]]]))
    # print(powerset([1, 2, 3]))
    print(subsequences([1, 2, 3]))
    # print(count)
    b = [5, 2, [7, 1], 3, [6, [13, 8], 4]]
    b1 = [1, [2, 3]]
    # print(productSum(b1))
    # print(powerset_recursive([1, 2,3]))
    print(powerset_backtracking([1, 2, 3]))
