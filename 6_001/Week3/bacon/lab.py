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
center_actor = 'Kevin Bacon'
names = [set()]

with open('resources/names.pickle', 'rb') as f:
    bacon_numbers_dict = pickle.load(f)
bacon_numbers = dict()
for key, value in bacon_numbers_dict.items():
    bacon_numbers[value] = key

#acted_together_names = defaultdict(list)
with open('resources/movies.pickle','rb') as f:
    movies = pickle.load(f)






def transform_data(raw_data):

    return set(raw_data)




acted_together_data = defaultdict(set)

def acted_together_ids(raw_data):
    for actor1, actor2, movie_id in raw_data:
        acted_together_data[actor1].add((actor2,movie_id))
        acted_together_data[actor2].add((actor1,movie_id))
    return acted_together_data

def acted_together(transformed_data, actor_id_1, actor_id_2):
    if actor_id_1 == actor_id_2:
        return False
    acted_together_ids(transformed_data)
    #todo Redo
    for actor2,_ in acted_together_data[actor_id_1]:#Incorrect, will check only the first value
        if actor2==actor_id_1 and actor2!=actor_id_1:
            return True
    for actor1,_ in acted_together_data[actor_id_2]:  # Incorrect, will check only the first value
        if actor1 == actor_id_2 and actor1 != actor_id_2:
            return True

    return False


# def dfs_for_bacon_ids(actor,visited,degree,temp,n):
#
#     if degree==n+1:
#         print(visited)
#         return temp
#
#     connections = [x for x in acted_together_data[actor]]
#
#
#     for current_actor,current_movie in connections:
#
#         if current_actor in visited: # This will make sure the current degree
#             continue
#         visited.add(current_actor)
#         temp.add(current_actor)
#
#         dfs_for_bacon_ids(current_actor,visited,degree+1,temp,n)
#         if degree==n+1:
#             #print(visited)
#             return temp
#         temp.remove(current_actor)
#     return temp if degree==n+1 else dfs_for_bacon_ids(actor,visited,degree+1,temp,n)


def actors_with_bacon_number(transformed_data, n):


    current_degree = 0
    # for actor1,actor2,movie in transformed_data:
    #     if actor1!=actor2:
    #         current=nodes.pop()
    #         if actor1==current:
    #             nodes.add(actor2)
    #             degree_of_separation[actor2].add(current_degree)
    #         elif actor2==current:
    #             nodes.add(actor1)
    #             degree_of_separation[actor1].add(current_degree)
    #         current_degree+=1
    bacon_ids = set()
    acted_together_ids(transformed_data)
    l = {x[0] for x in acted_together_data[center]}

    l = dict((0,)+(x,) for x in l)
    print(l)



    visited = set()
    #
    # for actor,movie in l:
    #     bacon_ids=dfs_for_bacon_ids(actor,visited,0,bacon_ids,n)
    #
    # print(bacon_ids)
    # BFS


    degree=0
    current=None
    while degree!=n+1:
        current=l[degree]
        for actor in current:
            if actor in visited:
                continue
            visited.add(actor)
            connections = {x[0] for x in acted_together_data[actor]}
            if connections:
                l[degree+1]=[c for c in connections if c not in visited]
                degree+=1
        return current
















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
    print(len(smalldb))
    s = set(smalldb)
    print(len(s))
    acted_together_ids(smalldb)
    print(acted_together_data[4724])
    a=acted_together_data[4724]
    for (a1,a2) in a:
        if a1==9207:
            print(a1,a2)
    # print(acted_together_data[center])
    # print(acted_together_data[center][0][0])
    # print([x[0] for x in acted_together_data[center]])
    #print(acted_together(smalldb,4724,9211))
    #print(actors_with_bacon_number(smalldb,2))


