"""
6.101 Lab:
Recipes
"""

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
                #("type element")
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

    def lowest_cost_helper1(lst, current_cost, quantity, compound_element, visited):

        flag = False
        if quantity:
            print("Compound:", compound_element, quantity)
            # #(compound_element)

            for elements in lst:

                for el in elements:
                    # if compound_element in cmpd_minimum_element_cost:
                    #     return current_cost
                    if type(el) == tuple:
                        el, q = el
                        # if el in visited:
                        #     continue

                        visited.add(el)
                        # if el == "cutting-edge laboratory":
                        #     continue
                        # (el)
                        if el in atomic_costs:
                            current_cost += atomic_costs[el] * q
                        elif el in cmpd_minimum_element_cost:
                            current_cost += cmpd_minimum_element_cost[el] * q
                            continue

                        else:
                            print("Inner:", el, end=" ")
                            # #(el)
                            lowest_cost_helper1(
                                list(compound_list[el]), current_cost, q, el, visited
                            )

            cmpd_minimum_element_cost[compound_element] = current_cost
            # if flag:
            #     flag = False
            #     break
            # (cmpd_minimum_element_cost)
            # (lst)

            current_cost *= quantity
            # (current_cost)
            return current_cost
        else:
            for elements in lst:
                for el in elements:
                    # (compound_element)
                    # if compound_element in cmpd_minimum_element_cost:
                    #     continue
                    if type(el) == tuple:
                        el, q = el
                        # if el in visited:
                        #     continue
                        visited.add(el)

                        # (el)
                        if el in atomic_costs:
                            current_cost += atomic_costs[el] * q
                            # (current_cost)
                        elif el in cmpd_minimum_element_cost:
                            current_cost += cmpd_minimum_element_cost[el] * q
                            continue

                        else:
                            print("Inner else:", el)
                            # (el)
                            lowest_cost_helper1(
                                list(compound_list[el]), current_cost, q, el, visited
                            )

                    # if flag:
                    #     flag = False
                    #     break
            cmpd_minimum_element_cost[compound_element] = current_cost

        # print(visited)

        # #(quantity) if quantity else #(current_cost)

        # (current_cost)
        # #(visited)
        return current_cost

    def lowest_compound_cost_helper(elements, element, cost, length):
        if not length:
            cmpd_minimum_element_cost[element] = (
                cost  # How does this guarantee min cost?
            )
            return cost
        for el in elements:
            if isinstance(el, tuple):
                if el[0] in atomic_costs:
                    cost += atomic_costs[el[0]] * el[1]
                    length -= 1
                    continue

                else:
                    new_elements = compound_list[el[0]]

        return cost

    atomic_costs = atomic_ingredient_costs(recipes)
    if food_item in atomic_costs:
        return atomic_costs[food_item]

    compound_list = compound_ingredient_possibilities(recipes)
    compounds = list(compound_list[food_item])[:]

    length = len(compounds)
    cmpd_minimum_element_cost = dict()
    min_cost = 100000000
    for i in range(length):
        print(compounds[i], "\n")
        current_cost = 0
        visited = set()
        for element, quantity in compounds[i]:
            # #(element)
            if element in atomic_costs:
                current_cost += atomic_costs[element] * quantity
                continue
            elif element in cmpd_minimum_element_cost:
                current_cost += cmpd_minimum_element_cost[element] * quantity
                input("Hi")
                continue
            else:
                elements_in_current = list(compound_list[element])[:]
                # current_cost += lowest_compound_cost_helper(elements_in_current, element, 0, len(elements_in_current))
                current_cost += (
                    lowest_cost_helper1(elements_in_current, 0, 0, None, visited)
                    * quantity
                )
            # (current_cost)
            # #(quantity)
        min_cost = min(current_cost, min_cost)

    # print(compounds,length)
    # print(compounds)
    # min_cost = 10000000
    #
    # total = []
    # min_current_cost = dict()
    # for i in range(length):
    #     visited = set()
    #     cost = []
    #     for el in compounds[i]:
    #         el, quantity = el
    #         if el in atomic_costs:
    #             cost.append(atomic_costs[el] * quantity)
    #         else:
    #             if el in visited:
    #                 cost.append(min_current_cost[el] * quantity)
    #                 continue
    #             visited.add(el)
    #             elements = compound_list[el]
    #             n = len(elements)
    #
    #             # lowest_cost_helper(compound_list[el],0,quantity,len(compound_list[el]))
    #     print()
    print(cmpd_minimum_element_cost)
    return min_cost


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
    atomic_ingredient_costs(example_recipes)
    c = compound_ingredient_possibilities(example_recipes)
    print(c["burger"])
    print(lowest_cost(example_recipes, "cheese"))
    # print("Cheese:", lowest_cost(example_recipes, "cheese"))  # Correct
    # assert lowest_cost(example_recipes, "time") == 10000
    # assert lowest_cost(example_recipes, "salt") == 1
    # assert abs(lowest_cost(example_recipes, "cornmeal") - 7.5) <= 1e-6
    #
    # # compound food items, only one layer deep
    # assert lowest_cost(example_recipes, "protein") == 100
    # assert lowest_cost(example_recipes, "cheese") == 10105
    # assert lowest_cost(example_recipes, "milk") == 105
    # # assert lowest_cost(example_recipes, "bread") == 9
    # assert lowest_cost(example_recipes, "burger") == 10685
    # two layers
    # print(lowest_cost(example_recipes, "burger"))
    # print(lowest_cost(dairy_recipes, "cheese"))
    print(lowest_cost(example_recipes, "burger"))
    # assert lowest_cost(example_recipes, "burger") == 10685
    # print("Bread:", lowest_cost(example_recipes, "bread"))
    # print("Lettuce:", lowest_cost(example_recipes, "lettuce"))
    # print("Cheese:", lowest_cost(example_recipes, "cheese"))
    # print("Protein:", lowest_cost(example_recipes, "protein"))
    # print("Ketchup:", lowest_cost(example_recipes, "ketchup"))
    # print("Chili:", lowest_cost(example_recipes, "beans"))
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
