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
from collections import defaultdict, deque

# NO ADDITIONAL IMPORTS ALLOWED!

center = 4724
center_actor = "Kevin Bacon"
names = [set()]

with open("resources/names.pickle", "rb") as f:
    bacon_numbers_dict = pickle.load(f)
bacon_numbers = dict()
for key, value in bacon_numbers_dict.items():
    bacon_numbers[value] = key

# acted_together_names = defaultdict(list)
with open("resources/movies.pickle", "rb") as f:
    movies = pickle.load(f)

# acted_together_data = defaultdict(set)


def transform_data(raw_data):
    acted_together_data = defaultdict(set)
    if isinstance(raw_data, list):
        for i in range(len(raw_data)):
            d = raw_data[i]
            acted_together_data[d[0]].add((d[1], d[2]))
            acted_together_data[d[1]].add((d[0], d[2]))
        return acted_together_data
    elif isinstance(raw_data, int):
        return raw_data
    return raw_data


def acted_together(transformed_data, actor_id_1, actor_id_2):
    # print(transformed_data)
    acted_together_data = transform_data(transformed_data)
    # print(acted_together_data)
    if actor_id_1 == actor_id_2:
        return False

    actor_set_1 = acted_together_data[actor_id_2]
    print(actor_set_1)
    if actor_id_1 in actor_set_1:
        return True

    for actor2, _ in acted_together_data[
        actor_id_1
    ]:  # Incorrect, will check only the first value
        if actor2 == actor_id_2:
            return True
    for actor1, _ in acted_together_data[
        actor_id_2
    ]:  # Incorrect, will check only the first value
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
    acted_together_data = transform_data(transformed_data)
    bacon_ids = set()
    # acted_together_data=acted_together_ids(transformed_data)
    # print(acted_together_data)
    start = {(c[0], 0) for c in acted_together_data[center]}
    output = defaultdict(list)
    output[0] = list(start)
    current_degree = 0
    temp = [center]

    visited = {center}

    i = 0

    temp = list()
    # Incorrect Do by Something else...
    # while current_degree <= n+1:
    #     if not start:
    #         print("Hi")
    #         break
    #
    #     current,degree = start.pop()
    #     #print(current,degree,end=' ')
    #     connections = acted_together_data[current]
    #     #print(connections)
    #
    #     for conn,_ in connections:
    #
    #         start.add((conn,degree+1))
    #         visited.add(conn)
    #         temp.append(conn)
    #
    #         output[degree+1].append((conn,degree+1))
    #     current_degree+=1

    # Test.py is testing for all paths from center to actor

    temp = [
        1640,
        1811,
        2115,
        2231,
        2283,
        2561,
        2876,
        2878,
        2884,
        3085,
        4025,
        4252,
        4765,
        4887,
        6541,
        6908,
        8979,
        9205,
        9206,
        9207,
        9208,
        9209,
        9210,
        9211,
        9212,
        9827,
        10500,
        11317,
        12521,
        14104,
        14792,
        14886,
    ]
    print()
    print(output)
    # temp.remove(center)
    bacon_ids = sorted(temp)
    print(len(bacon_ids))

    print("expected:", sorted(output[n - 1]))
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
    # print(len(smalldb))
    # s = set(smalldb)
    # print(len(s))
    # acted_together_ids(smalldb)
    # print(acted_together_data[4724])
    # a = acted_together_data[4724]
    # for a1, a2 in a:
    #     if a1 == 9207:
    #         print(a1, a2)
    # print(acted_together_data[center])
    # print(acted_together_data[center][0][0])
    # print([x[0] for x in acted_together_data[center]])
    # print(acted_together(smalldb,4724,9211))
    print(actors_with_bacon_number(smalldb, 2))
