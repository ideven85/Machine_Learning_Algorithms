"""
Question 3: Write the body of the tree_list function below.

You may test this function by running
`pytest q3_tree_list.py -v`
without quotes.

Is there a way you can write this function that requires
sorting the result only once?
"""

from debug_recursion import show_recursive_structure

count = 0
@show_recursive_structure
def tree_list(tree):
    """
    Given tree as a dict { 'value': number,
                           'children': list of trees },
    return a sorted list of all the values found in the tree (from
    smallest to largest).
    """
    global count
    if not tree:
        return []
    if type(tree) is list:
        print("Hi1",tree)
        return tree[0]
    count+=1
    value = tree['value']
    children = tree['children']

    if len(children) == 0:
        return value

    if type(children) is list and len(children):
        #print("Hi",[tree_list(x) for x in children])
        mid_operation = tree_list(children)
        if type(mid_operation) is list:
            print("Hi",mid_operation)
            mid_operation= mid_operation.append(value)
            return mid_operation
        else:
            print("Hi3")
            return [mid_operation]+[value]
    print("Hi2")
    return value+children

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
                {"value": 16, "children": []},#{"value": 7, "children": []}
                {"value": 42, "children": []},
            ],
        },
    ],
}


# def test_tree_list():
#     assert tree_list(t1) == [3]
#     assert tree_list(t2) == [2, 3, 7, 9]
#     #assert tree_list(t3) == [2, 3, 7, 9, 16, 42, 99]
#     print("correct!")


if __name__ == "__main__":
    # uncomment the @show_recursive_structure line
    # above the function to see some detailed function output
    print(tree_list(t3))