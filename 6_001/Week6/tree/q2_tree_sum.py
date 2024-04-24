"""
Question 2: Write the body of the tree_sum function below.

You may test this function by running
`pytest q2_tree_sum.py -v`
without quotes.
"""

# from debug_recursion import show_recursive_structure


def tree_sum(tree):
    """
    Given tree as a dict { 'value': number,
                           'children': list of trees },
    return the sum of all the values found in the tree.
    """

    sum_so_far = 0
    if not tree:
        return sum_so_far
    # Convert tree to List

    agenda = [tree]
    while agenda:
        x = agenda.pop(-1)
        print(x)
        if not x:
            sum_so_far += 0

        elif isinstance(x[0], dict):
            sum_so_far += x[0]["value"]
            agenda.append(x[0]["children"])

        else:
            sum_so_far += x["value"]
    return sum_so_far


t1 = {"value": 3, "children": []}

t2 = {
    "value": 9,
    "children": [
        {"value": 2, "children": []},
        {"value": 3, "children": []},
        {"value": 7, "children": []},
    ],
}

t3 = {
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


def test_tree_sum():
    assert tree_sum(t1) == 3
    assert tree_sum(t2) == 21
    assert tree_sum(t3) == 178
    print("correct!")


if __name__ == "__main__":
    # uncomment the @show_recursive_structure line
    # above the function to see some detailed function output
    print(tree_sum(t2))
