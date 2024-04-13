tree1 = [13, [7], [8, [99], [16, [77]], [42]]]


def all_values(tree):
    if not tree:
        return

    parent = tree[0]
    children = tree[1:]
    if not children:
        return parent
    if len(children) == 1:
        yield parent, children[0]

    elif isinstance(children[0], list):
        yield all_values(children[0]), all_values(children[1:])
    else:

        yield children[0], all_values(children[1:])


print(list(all_values(tree1)))
