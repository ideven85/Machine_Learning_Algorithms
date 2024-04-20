"""
6.101 Lab 3:
Bacon Number
"""

"""
Remember 10 hours per lab at least
Do all labs
"""

#!/usr/bin/env python3

import pickle
#from collections import defaultdict, deque

# NO ADDITIONAL IMPORTS ALLOWED!
#
# center = 4724
# center_actor = "Kevin Bacon"
# names = [set()]
#
# with open("resources/names.pickle", "rb") as f:
#     bacon_numbers_dict = pickle.load(f)
# bacon_numbers = dict()
# for key, value in bacon_numbers_dict.items():
#     bacon_numbers[value] = key
#
# # acted_together_names = defaultdict(list)
# with open("resources/movies.pickle", "rb") as f:
#     movies = pickle.load(f)
#
# # acted_together_data = defaultdict(set)
#

def transform_data(raw_data):
    data = dict()
    if isinstance(raw_data, list):
        for actor1, actor2, film in  raw_data:
            data.setdefault(actor1, set()).add((actor2, film))
            data.setdefault(actor2, set()).add((actor1, film))
        return data
    elif isinstance(raw_data, int):
        return raw_data
    return raw_data


def acted_together(transformed_data, actor_id_1, actor_id_2):
    # print(transformed_data)
    acted_together_data = transform_data(transformed_data)
    # print(acted_together_data)
    if actor_id_1 == actor_id_2:
        return True

    actor_set_1 = acted_together_data[actor_id_2]
    #print(actor_set_1)
    if actor_id_1 in actor_set_1:
        return True

    for actor2, _ in acted_together_data[
        actor_id_1
    ]:
        if actor2 == actor_id_2:
            return True
    for actor1, _ in acted_together_data[
        actor_id_2
    ]:
        if actor1 == actor_id_1:
            return True

    return False


def dfs_for_bacon_ids(acted_together_data, actor, visited, degree, output, n):

    if degree == n:

        return output[n]
    connections = acted_together_data[actor]
    for conn, movie in connections:
        # Does the graph contain cycles?
        output[degree].add(conn)
        dfs_for_bacon_ids(acted_together_data, conn, visited, degree + 1, output, n)


def actors_with_bacon_number(transformed_data, n):
    """
    n is the smallest number of films separating the actors from center 4724
    """
    acted_together_data = transform_data(transformed_data)
    bacon_ids = set()
    center=4724
    # acted_together_data=acted_together_ids(transformed_data)
    # print(acted_together_data)
    start = {(c[0], 0) for c in acted_together_data[center]}
    output =dict()
    output[0] = list(start)
    current_degree = 0
    temp = [center]

    visited = {center}


    for i in range(n):
        df

    temp = list()



    return bacon_ids


def bacon_path(transformed_data, actor_id):
    raise NotImplementedError("Implement me!")


def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")


def actor_path(transformed_data, actor_id_1, goal_test_function):
    raise NotImplementedError("Implement me!")


def actors_connecting_films(transformed_data, film1, film2):
    raise NotImplementedError("Implement me!")


if __name__ == "__main__":
    with open("resources/small.pickle", "rb") as f:
        smalldb = pickle.load(f)

    with open('resources/tiny.pickle',"rb") as f:
        tiny_data = pickle.load(f)

    # print(tiny_data)
    # print(acted_together(tiny_data,4724,1640))
    #print(actors_with_bacon_number(tiny_data, 0))
    data = {}
    for actor1, actor2,film in tiny_data:
        data.setdefault(actor1,set()).add((actor2,film))
        data.setdefault(actor2,set()).add((actor1,film))

    # print(data)

    bacon_id_0 =  {x for x,y in data[4724]}
    # center = 4724
    # for actor,_ in data[4724]:
    #     bacon_id_0.add(actor)
    # print(bacon_id_0)

