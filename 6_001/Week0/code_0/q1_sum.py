def sum_lists(lists):
    """
    Given a list of lists of numbers, return a new list where each list 
    is replaced by the sum of its elements without modifying the input list.
    """
    output = [0] * len(lists)
    for i in range(len(lists)):
        total = 0
        for i in lists[i]:
            total += i
        output[i] = total
    return output

#inp = [ [# some numbers], ... ]
#exp = [ ... # some numbers ]
#out = sum_lists(inp)
#print(out)