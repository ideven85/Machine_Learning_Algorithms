def sum_nested(x):
    if not x:
        return 0
    elif isinstance(x[0], list):
        return sum_nested(x[0]) + sum_nested(x[1:])
    else:
        return x[0] + sum_nested(x[1:])


def tree_sum(tree):
    """

    >>>t1 = {"value": 3, "children": []}

    >>>t2 = {
        "value": 9,
        "children": [
            {"value": 2, "children": []},
            {"value": 3, "children": []},
            {"value": 7, "children": []},
        ],
    }

    >>>t3 = {
        "value": 9,
        "children": [
            {"value": 2, "children": []},
            {
                "value": 3,
                "children": [
                    {"value": 99, "children": []},
                    {"value": 16, "children": [{"value": 7, "children": []}]},
                    {"value": 42, "children": []},
                ],
            },
        ],
    }
        >>> tree_sum(t1)==3
        >>> tree_sum(t2) == 21
        >>> tree_sum(t3) == 178
    """
    if not tree:
        return 0
    elif not tree["children"]:
        return tree["value"]
    else:
        return tree["value"] + sum(
            tree_sum(x) for x in tree["children"]
        )  # Generator version going deeper into the tree


print(sum_nested([1, [2, [3, [[[4]]]]]]))
tree1 = {"value": 9, "children": []}

print(tree_sum(tree1))
