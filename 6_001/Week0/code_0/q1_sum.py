def sum_lists(lists):
    """
    Given a list of lists of numbers, return a new list where each list
    is replaced by the sum of its elements without modifying the input list.
    """

    output = []
    for i in range(len(lists)):
        total = 0

        for val in lists[i]:
            total += val
        output.append(total)
    return output

def sum_nested_lists(lists):
    out=[]
    current=0
    if not lists:
        return 0
    elif isinstance(lists[0], list):
        return sum_nested_lists(lists[0])+sum_nested_lists(lists[1:])
    else:
        return lists[0]+sum_nested_lists(lists[1:])

# inp = [ [# some numbers], ... ]
# exp = [ ... # some numbers ]
# out = sum_lists(inp)
# print(out)

lst = [[1,2],[3,4],[5,6],7]
print(sum_lists(lst))

print(sum_nested_lists(lst))