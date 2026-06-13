def sum_lists(lists):
    """
    Given a list of lists of numbers, return a new list where each list
    is replaced by the sum of its elements without modifying the input list.
    """

    def sum_list_helper(lst, i, sum_so_far):
        if i >= len(lst):
            return sum_so_far
        sum_so_far += lst[i]
        return sum_list_helper(lst, i + 1, sum_so_far)

    return sum_list_helper(lists, 0, 0)


def sum_nested_lists(lists):
    out = []
    current = 0
    if not lists:
        return 0
    elif isinstance(lists[0], list):
        return sum_nested_lists(lists[0]) + sum_nested_lists(lists[1:])
    else:
        return lists[0] + sum_nested_lists(lists[1:])


# inp = [ [# some numbers], ... ]
# exp = [ ... # some numbers ]
# out = sum_lists(inp)
# print(out)

lst = [[1, 2], [3, 4], [5, 6], 7]
print(sum_lists([1, 2, 3]))

print(sum_nested_lists(lst))
