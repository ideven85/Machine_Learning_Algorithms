def flatten(x):
    out = []
    for elt in x:
        if isinstance(elt, list):
            out.extend(flatten(elt))
        else:
            out.append(elt)
    return out
x = [1, [2, [3, [4]]]]
y = [[[[[[[1, 2, 3]]]]], 4], 5]
print(flatten(x))
print(flatten(y))