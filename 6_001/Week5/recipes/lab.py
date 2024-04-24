"""
6.101 Lab:
Recipes
"""

import pickle
import sys

sys.setrecursionlimit(20_000)
# NO ADDITIONAL IMPORTS!
# Min 10 hours per lab, Don't get disheartened in one day


def atomic_ingredient_costs(recipes):
    """
    Given a recipes list, make and return a dictionary mapping each atomic food item
    name to its cost.
    """
    atomic_recipes = dict()
    for recipe in recipes:

        if recipe[0] == "atomic":
            atomic_recipes[recipe[1]] = recipe[2]
    return atomic_recipes


def compound_ingredient_possibilities(recipes):
    """
    Given recipes, a list containing compound and atomic food items, make and
    return a dictionary that maps each compound food item name to a list
    of all the ingredient lists associated with that name.
    """
    # raise NotImplementedError
    cmpd = dict()
    for r in recipes:
        if r[0] == "compound":
            cmpd.setdefault(r[1], []).append(r[2])
    # print("In upper:",cmpd['cheese'][0],cmpd['cheese'][1])
    # print(cmpd['milk'])
    # print(cmpd['cheese'])
    return cmpd


"""
            if isinstance(element,tuple):
                #print("Hi2",*element,end=' ')
                element,quantity=element
                if element in costs:
                    current_cost[0]+=costs[element]*quantity
                    print(current_cost,"Tuple")

                else:
                    print(element,quantity,"Hi")

                    if isinstance(element, tuple):
                        el, q = element

                        current_cost[0] += costs[el]*q
                    else:
                        print(element,quantity,list(compound_list[element]))

                        current_cost[0]+=lowest_cost_helper(list(compound_list[element]),cost,current_cost)*quantity
                print(current_cost)
                input("type element")
                #print(current_cost, "Recursive")
                # return current_cost[0]+cost[0]
            #print(current_cost)
        return cost[0]+current_cost[0]
"""


def lowest_cost(recipes, food_item):
    """
    Given a recipes list and the name of a food item, return the lowest cost of
    a full recipe for the given food item.
    """
    # raise NotImplementedError

    def lowest_cost_helper(lst, cost, current_cost, quantity, visited):
        # print(lst,quantity)
        if isinstance(lst, tuple):
            el, q = lst
            if el in costs:
                current_cost[0] = current_cost[0] + costs[el] * q
            else:
                elements = list(compound_list[el])
                for el in elements:
                    lowest_cost_helper(el, cost, current_cost, quantity, visited)
        else:
            for elements in lst:
                for el in elements:
                    if type(el) == tuple:
                        el, q = el
                        if el in costs:
                            current_cost[0] += costs[el] * q
                        else:
                            lowest_cost_helper(el, cost, current_cost, q, visited)

        # print(visited)
        # print(current_cost)
        return current_cost

    costs = atomic_ingredient_costs(recipes)
    if food_item in costs:
        return costs[food_item]

    compound_list = compound_ingredient_possibilities(recipes)
    compounds = list(compound_list[food_item])[:]
    length = len(compounds)

    # print(compounds,length)
    # print(compounds)
    min_cost = 10000000

    total = []
    for i in range(length):
        cost = [0]
        for el in compounds[i]:
            el, quantity = el
            if el in costs:

                cost[0] += costs[el] * quantity
            else:

                temp = lowest_cost_helper(
                    list(compound_list[el]), cost, [0], quantity, {}
                )
                cost[0] += temp[:][0]
                # Need to implement min here alsp
                print(temp)
                input(el)

        # current=[0]
        # #print(compounds[i])
        # lowest_cost_helper(compounds[i],cost,current)
        # input(current)
        # total[i]=current[:][0]
        # input(total)
        # print(current,cost)
        min_cost = min(cost[0], min_cost)
        total.append(cost[:][0])
        cost.clear()
    print(total)
    print("Min:", min_cost)
    return min(total)


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
    # with open("test_recipes/example_recipes.pickle", "rb") as f:
    #     example_recipes = pickle.load(f)
    # you are free to add additional testing code here!
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
                ("bread", 1),
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

    dairy_recipes = [
        ("compound", "milk", [("cow", 2), ("milking stool", 1)]),
        ("compound", "cheese", [("milk", 1), ("time", 1)]),
        ("compound", "cheese", [("cutting-edge laboratory", 11)]),
        ("atomic", "milking stool", 5),
        ("atomic", "cutting-edge laboratory", 1000),
        ("atomic", "time", 10000),
        ("atomic", "cow", 100),
    ]
    atomic_ingredient_costs(dairy_recipes)
    # compound_ingredient_possibilities(dairy_recipes)
    print("Burger:", lowest_cost(example_recipes, "burger"))  # Wrong
    print("Bread:", lowest_cost(example_recipes, "bread"))
    print("Lettuce:", lowest_cost(example_recipes, "lettuce"))
    print("Cheese:", lowest_cost(example_recipes, "cheese"))
    print("Protein:", lowest_cost(example_recipes, "protein"))
    print("Ketchup:", lowest_cost(example_recipes, "ketchup"))
    print("Chili:", lowest_cost(example_recipes, "beans"))
    #
    # print(lowest_cost(dairy_recipes,'cow'))
    # print(lowest_cost(dairy_recipes,'cheese'))
    # print(dairy_recipes)
    cookie_recipes = [
        ("compound", "cookie sandwich", [("cookie", 2), ("ice cream scoop", 3)]),
        ("compound", "cookie", [("chocolate chips", 3)]),
        ("compound", "cookie", [("sugar", 10)]),
        ("atomic", "chocolate chips", 200),
        ("atomic", "sugar", 5),
        ("compound", "ice cream scoop", [("vanilla ice cream", 1)]),
        ("compound", "ice cream scoop", [("chocolate ice cream", 1)]),
        ("atomic", "vanilla ice cream", 20),
        ("atomic", "chocolate ice cream", 30),
    ]
    # print(lowest_cost(cookie_recipes, 'cookie sandwich'))
