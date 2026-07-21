def first_occurrence(data):
    """
    Given a list of integers or strings, return a new list with the same
    set of items in the same order, but keeping only the first occurrence of
    each item.
    >>> first_occurrence([1, 9, 1, 1, 5, 3, 2, 9, 10]) == [1, 9, 5, 3, 2, 10]
    True
    """
    visited = set()
    output = []
    for val in data:
        if val in visited:
            continue
        visited.add(val)
        output.append(val)
    return output


def how_old(data):
    """
    Given a list of integers or strings, returns a list of the same length
    where the ith entry is the distance of the ith entry in the input list
    to the last occurrence of the same value in the input list,
    or None if there was no previous occurrence.
    >>> how_old([1, 2, 1, 1, 2]) == [None, None, 2, 1, 3]
    True
    """
    mapping = dict()
    output = []
    for index, value in enumerate(data):
        if value not in mapping:
            # print(index,value)
            mapping[value] = index
            output.append(None)
        else:
            last_index = mapping[value]
            # print(last_index,index)
            output.append((index - last_index))
            mapping[value] = index
    return output


import doctest

if __name__ == "__main__":
    print(how_old([1, 2, 1, 1, 2]))
