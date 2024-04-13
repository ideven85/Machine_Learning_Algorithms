def flatten(x):

    for elt in x:
        if isinstance(elt, list):
            yield from flatten(elt)
            # print(out)

        else:
            yield elt


x = [1, [2, [3, [4]]]]
y = [[[[[[[1, 2, 3]]]]], 4], 5]
print(list(flatten(x)))
print(list(flatten(y)))
# print(flatten(y))
