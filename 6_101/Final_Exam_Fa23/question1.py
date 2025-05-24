def swap_pairs(inp, index=0, temp=None):
    if not temp:
        temp = inp[:]
    if index >= len(inp) - 1:
        return temp

    temp[index], temp[index + 1] = temp[index + 1], temp[index]

    swap_pairs(inp, index + 2, temp)
    return temp


def swap_pairs_given_code(inp):
    if len(inp) < 2:
        return inp[:]
    return [inp[1], inp[0]] + swap_pairs_given_code(inp[2:])  # More Pythonic


a = [1, 2]
print(swap_pairs(a))
print(swap_pairs_given_code(a))
