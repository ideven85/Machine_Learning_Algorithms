def flatten(x):
    out = []
    for elt in x:
        if isinstance(elt, list):
            out.extend(flatten(elt))
            #print(out)

        else:
            out.append(elt)
            print(out)

    return out


x = [1, [2, [3, [4]]]]
y = [[[[[[[1, 2, 3]]]]], 4], 5]
# print(list(flatten(x)))
print(flatten(y))
#print(flatten(y))
