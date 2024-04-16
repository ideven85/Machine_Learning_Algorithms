"""
6.101 Lab 5:
Recipes
"""

import pickle
import sys
from collections import defaultdict

# 10 hours per lab

sys.setrecursionlimit(20_000)
# NO ADDITIONAL IMPORTS!


def atomic_ingredient_costs(recipes):
    """
    Given a recipes list, make and return a dictionary mapping each atomic food item
    name to its cost.
    """
    atomic_dictionary = dict()
    for recipe in recipes:
        if recipe[0] == "atomic":
            atomic_dictionary[recipe[1]] = recipe[2]

    return atomic_dictionary


def compound_ingredient_possibilities(recipes):
    """
    Given recipes, a list containing compound and atomic food items, make and
    return a dictionary that maps each compound food item name to a list
    of all the ingredient lists associated with that name.
    """
    compound_dictionary = defaultdict(list)
    for r in recipes:
        if r[0] == "compound":
            compound_dictionary[r[1]].append(r[2])
    return compound_dictionary


def lowest_cost(recipes, food_item):
    """
    Given a recipes list and the name of a food item, return the lowest cost of
    a full recipe for the given food item.
    """
    atomic_dictionary = atomic_ingredient_costs(recipes)
    compound_dictionary = compound_ingredient_possibilities(recipes)

    def lowest_cost_helper():
        cost1 = 10000000000
        cost2 = 10000000
        if food_item in atomic_dictionary:
            cost1 = atomic_dictionary[food_item]
        if food_item in compound_dictionary:
            compounds = compound_dictionary[food_item]

            current = 0

            cost2 = min(current, cost2)
        print(cost1, cost2)
        return min(cost1, cost2)

    return lowest_cost_helper()


def scaled_flat_recipe(flat_recipe, n):
    """
    Given a dictionary of ingredients mapped to quantities needed, returns a
    new dictionary with the quantities scaled by n.
    """
    raise NotImplementedError


def add_flat_recipes(flat_recipes):
    """
    Given a list of flat_recipe dictionaries that map food items to quantities,
    return a new overall 'grocery list' dictionary that maps each ingredient name
    to the sum of its quantities across the given flat recipes.

    For example,
        add_flat_recipes([{'milk':1, 'chocolate':1}, {'sugar':1, 'milk':2}])
    should return:
        {'milk':3, 'chocolate': 1, 'sugar': 1}
    """
    raise NotImplementedError


def cheapest_flat_recipe(recipes, food_item):
    """
    Given a recipes list and the name of a food item, return a dictionary
    (mapping atomic food items to quantities) representing the cheapest full
    recipe for the given food item.

    Returns None if there is no possible recipe.
    """
    raise NotImplementedError


def combined_flat_recipes(flat_recipes):
    """
    Given a list of lists of dictionaries, where each inner list represents all
    the flat recipes for a certain ingredient, compute and return a list of flat
    recipe dictionaries that represent all the possible combinations of
    ingredient recipes.
    """
    raise NotImplementedError


def all_flat_recipes(recipes, food_item):
    """
    Given a list of recipes and the name of a food item, produce a list (in any
    order) of all possible flat recipes for that category.

    Returns an empty list if there are no possible recipes
    """
    raise NotImplementedError


if __name__ == "__main__":
    # load example recipes from section 3 of the write-up

    example_recipes = [
        (
            "compound",
            "chili",
            [
                ("beans", 3),
                ("cheese", 10),
                ("chili powder", 1),
                ("cornbread", 2),
                ("protein", 1),
            ],
        ),
        ("atomic", "beans", 5),
        (
            "compound",
            "cornbread",
            [("cornmeal", 3), ("milk", 1), ("butter", 5), ("salt", 1), ("flour", 2)],
        ),
        ("atomic", "cornmeal", 7.5),
        (
            "compound",
            "burger",
            [
                ("bread", 2),
                ("cheese", 1),
                ("lettuce", 1),
                ("protein", 1),
                ("ketchup", 1),
            ],
        ),
        (
            "compound",
            "burger",
            [
                ("bread", 2),
                ("cheese", 2),
                ("lettuce", 1),
                ("protein", 2),
            ],
        ),
        ("atomic", "lettuce", 2),
        ("compound", "butter", [("milk", 1), ("butter churn", 1)]),
        ("atomic", "butter churn", 50),
        ("compound", "milk", [("cow", 1), ("milking stool", 1)]),
        ("compound", "cheese", [("milk", 1), ("time", 1)]),
        ("compound", "cheese", [("cutting-edge laboratory", 11)]),
        ("atomic", "salt", 1),
        ("compound", "bread", [("yeast", 1), ("salt", 1), ("flour", 2)]),
        ("compound", "protein", [("cow", 1)]),
        ("atomic", "flour", 3),
        ("compound", "ketchup", [("tomato", 30), ("vinegar", 5)]),
        ("atomic", "chili powder", 1),
        (
            "compound",
            "ketchup",
            [
                ("tomato", 30),
                ("vinegar", 3),
                ("salt", 1),
                ("sugar", 2),
                ("cinnamon", 1),
            ],
        ),  # the fancy ketchup
        ("atomic", "cow", 100),
        ("atomic", "milking stool", 5),
        ("atomic", "cutting-edge laboratory", 1000),
        ("atomic", "yeast", 2),
        ("atomic", "time", 10000),
        ("atomic", "vinegar", 20),
        ("atomic", "sugar", 1),
        ("atomic", "cinnamon", 7),
        ("atomic", "tomato", 13),
    ]

    # for recipe in example_recipes:
    #     if recipe[0] == "compound":
    #         print(*recipe)
    #     else:
    #         print(*recipe)
    # you are free to add additional testing code here!
    a = atomic_ingredient_costs(example_recipes)
    print(sum(a.values()))
    b = compound_ingredient_possibilities(example_recipes)
    print(b)
    dairy_recipes = [
        ("compound", "milk", [("cow", 2), ("milking stool", 1)]),
        ("compound", "cheese", [("milk", 1), ("time", 1)]),
        ("compound", "cheese", [("cutting-edge laboratory", 11)]),
        ("atomic", "milking stool", 5),
        ("atomic", "cutting-edge laboratory", 1000),
        ("atomic", "time", 10000),
        ("atomic", "cow", 100),
    ]
    print(lowest_cost(dairy_recipes, "cheese"))
