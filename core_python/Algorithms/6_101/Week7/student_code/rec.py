# 6.101 recitation
import copy
from collections import defaultdict


############################################ potluck

# You are organizing a potluck for your friends, and you want to make sure that
# everybody who comes to your party has something that they can eat!
#
# Given a dictionary containing food preferences (mapping person => list of
# foods they will eat), and a dictionary containing the food you have available
# (mapping food name => quantity), we want to give everybody one food in their
# preferences, but we can't give out more of a particular food than we have
# available at the start.


def feed(preferences: dict, quantities: dict):
    """
    >>> out1 = {'alex': 'pickles', 'billie': 'ketchup'}
    >>> feed({'alex': ['pickles'], 'billie': ['ketchup']},
    ...      {'pickles': 1, 'ketchup': 1}) == out1
    True

    >>> feed({'alex': ['pickles'], 'billie': ['pickles']},
    ...      {'pickles': 1, 'ketchup': 1}) is  None
    True

    >>> out2 = {'alex': 'pickles', 'billie': 'pickles'}
    >>> feed({'alex': ['pickles'], 'billie': ['pickles']},
    ...      {'pickles': 2, 'ketchup': 1}) == out2
    True

    >>> preferences = {'alex': ['pickles', 'ketchup'], 'billie': ['chips', 'onions'],
    ...           'cameron': ['pie', 'broccoli'],  'devin': ['pickles'],
    ...           'emery': ['onions'], 'frankie': ['pie']}
    >>> foods = {'pickles': 1, 'ketchup': 1, 'chips': 1, 'onions': 1,
    ...          'pie': 1, 'broccoli': 1}
    >>> expected = {'alex': 'ketchup', 'billie': 'chips', 'cameron': 'broccoli',
    ...             'devin': 'pickles', 'emery': 'onions', 'frankie': 'pie'}
    >>> feed(preferences, foods) == expected
    True

    >>> preferences = {'alex': ['cake', 'cheese', 'pie', 'sandwiches'],
    ...           'billie': ['cake', 'cheese', 'pie'],
    ...           'cameron': ['cake', 'cheese'],
    ...           'devin': ['cake', 'cheese'],
    ...           'emery': ['cake', 'cheese']}
    >>> foods = {'cake': 2, 'cheese': 1, 'pie': 1, 'sandwiches': 1}
    >>> res = feed(preferences, foods)
    >>> res['alex'], res['billie']
    ('sandwiches', 'pie')
    >>> sorted((res['cameron'], res['devin'], res['emery']))
    ['cake', 'cake', 'cheese']
    """

    # Solution 1

    def dfsUtil(
        person,
        foods_available,
        quantities_available,
        visited,
        possiblities=defaultdict(),
    ):

        f = foods_available
        if quantities_available[f] and f not in visited:
            # possiblities[person].append(f)
            if quantities_available[f]:
                possiblities[person] = f
                quantities_available[f] -= 1

                visited.add(f)
        print(visited)
        return possiblities

    names, liked_food_list = [name for name in preferences.keys()], [
        val for val in preferences.values()
    ]
    foods_available, food_quantity_available = [food for food in quantities.keys()], [
        val for val in quantities.values()
    ]
    q = {
        k: v
        for k, v in sorted(
            zip(foods_available, food_quantity_available),
            key=lambda x: x[1],
            reverse=True,
        )
    }
    output = dict()
    visited = set()
    n = len(names)
    for i in range(n):
        agenda = names[i]
        liked_foods = liked_food_list[i]
        # print("x",liked_foods)
        for x in liked_foods:

            # print(x,end=' ')

            choices = dfsUtil(agenda, x, q, visited)
            # if len(choices)>1:
            #     print("HI",end=' ')
            #     print(choices,end=' ')
            #     output[tuple(choices.keys())[0]]=list(choices.values())[0]

            if choices:
                # print(choices)
                if agenda not in output:
                    for val in choices.values():

                        if val in preferences[agenda]:
                            # print(val)
                            output[agenda] = val

        # print(output)
        # print(choices)
    print("V", visited)
    return output


"""
Exercise: develop a STRATEGY to implement this

* Base case(s)?

* What kind of things need to be tried? i.e., how can
  the search proceed one step at a time?

* What are recursive case(s)? How does the problem get
  smaller on each step/recursion?

* How to detect and handle when the recursion fails?
"""


import doctest

if __name__ == "__main__":
    preferences, foods = (
        {"alex": ["pickles"], "billie": ["pickles"]},
        {"pickles": 1, "ketchup": 1},
    )
    print(feed(preferences, foods))
    # preferences1 = {'alex': ['cake', 'cheese', 'pie', 'sandwiches'], 'billie': ['cake', 'cheese', 'pie'],'cameron': ['cake', 'cheese'],'devin': ['cake', 'cheese'],'emery': ['cake', 'cheese']}
    # foods1 = {'cake': 2, 'cheese': 1, 'pie': 1, 'sandwiches': 1}
    # print(feed(preferences1,foods1))
    # preferences2={'alex': ['pickles'], 'billie': ['ketchup']}
    # foods2 = {'pickles': 1, 'ketchup': 2}
    # print(feed(preferences2,foods2))
    people = {"alex": ["salad", "burger"], "tim": ["salad"]}
    food = {"burger": 1, "salad": 1}
    print(feed(people, food))
