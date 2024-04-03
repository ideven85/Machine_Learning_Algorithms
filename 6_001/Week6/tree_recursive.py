def sum_nested_list(tree):
    if not tree:
        return 0
    elif isinstance(tree[0],list):
        return sum_nested_list(tree[0])+sum_nested_list(tree[1:])
    else:
        return tree[0]+sum_nested_list(tree[1:])




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
nested_tree1=[3,[]]
nested_tree2=[[9,[[2,[]],[3,[]],[7,[]]]]]
nested_tree3 =[9,[[2,[]],[3,[99,[]],[16,[7,[]]],[42,[]]]]]
print(sum_tree(nested_tree1))
print(sum_tree(nested_tree2))
print(sum_tree(nested_tree3))