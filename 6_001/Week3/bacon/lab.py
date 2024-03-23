"""
6.101 Lab 3:
Bacon Number
"""

#!/usr/bin/env python3

import pickle
from collections import defaultdict

# NO ADDITIONAL IMPORTS ALLOWED!

bacon_numbers = list(dict)

def transform_data(raw_data):
    #bacon_numbers=[defaultdict(list) for _ in range(len(raw_data))]
    print(type(raw_data))
    for i in range(len(raw_data)):
        bacon_numbers.append(raw_data[i][0])
        bacon_numbers[raw_data[i][0]].append(raw_data[i][1])
        bacon_numbers[raw_data[i][0]].append(raw_data[i][2])
        bacon_numbers[raw_data[i][1]].append(raw_data[i][0])
        bacon_numbers[raw_data[i][1]].append(raw_data[i][2])
    return bacon_numbers
def get_names_with_bacon_numbers(transformed_data):
    pass

# def get_names(raw_data):
#     names = [{}]
#     for line in raw_data:
#         temp = set()
#         temp.add(bacon_numbers.get(line[0]))
#         temp.add(bacon_numbers.get(line[1]))
#         temp.add(line[2])
#         names.append(temp)
#     return names




def acted_together(transformed_data, actor_id_1, actor_id_2):
    actor1 = bacon_numbers[actor_id_1]
    actor2 = bacon_numbers[actor_id_2]



def actors_with_bacon_number(transformed_data, n):
    raise NotImplementedError("Implement me!")


def bacon_path(transformed_data, actor_id):
    raise NotImplementedError("Implement me!")


def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    raise NotImplementedError("Implement me!")


def actor_path(transformed_data, actor_id_1, goal_test_function):
    raise NotImplementedError("Implement me!")


def actors_connecting_films(transformed_data, film1, film2):
    raise NotImplementedError("Implement me!")


if __name__ == "__main__":
    file_name = "acted_together.txt"
    smalldb=None
    with open("resources/small.pickle", "rb") as f:
        db_small = pickle.load(f)
    a=transform_data(db_small)
    print(a)
    # with open(file_name,'w') as f:
    #     for actor in db_small:
    #         f.write(str(actor[0])+ ',' + str(actor[1])+','+str(actor[2])+'\n')





    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.

