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



#todo Implement This

def actors_with_bacon_number(transformed_data, n):
    """
    n is the smallest number of films separating the actors from center 4724
    """

    #Redo
    def dfs_for_bacon_ids(actor, visited_actors,visited_films, current_degree, current_actors):

        if current_degree>n:
            #print("C",current_actors)

            return current_actors

        current_actors.append(actor)
        connections= acted_together_data[actor]
        if not connections:
            return current_actors
        #print(connections)
        for conn,film in connections:
            if conn in visited_actors:
                continue
            visited_actors.add(conn)

            current_actors.append(conn)
            return dfs_for_bacon_ids(conn, visited_actors,visited_films, current_degree+1, current_actors)
        return current_actors
    acted_together_data = transform_data(transformed_data)

    center=4724
    # acted_together_data=acted_together_ids(transformed_data)
    # print(acted_together_data)
    agenda = [center]
    # output = [[]]
    #
    # output[0] = list(start.keys())
    final_path=None
    current_degree = 0
    final_actors = []
    visited_actors = set()
    while current_degree!=n+1:

        current_actors = []


        if not agenda:
            input()
            #print("Please:",sorted(final_actors))
            break
        current_actor=agenda.pop(0)

        if current_actor not in acted_together_data:
            continue
        connections= acted_together_data[current_actor]

        for actor,_ in connections:

            current_actors=dfs_for_bacon_ids(actor,visited_actors,set(),current_degree,current_actors)

            if current_actors is not None:
                print((sorted(set(current_actors))), current_degree, len(set(current_actors)))




                for s in current_actors:
                    agenda.append(s)



        #current_actors=[]

        current_degree+=1
    #print(output)

    out=set()
    # while current_degree<=n:
    #
    #     this_path = agenda.pop(0)
    #     # terminal_state = this_path[-1]
    #     # print(terminal_state)
    #     # if current_degree==n:
    #     #     final_path=this_path
    #     #     break
    #     neighbours = transformed_data[this_path]
    #     print(neighbours)
    #     for connection,film in neighbours:
    #         # if connection in visited:
    #         #     continue
    #         visited.add(connection)
    #
    #         agenda.append(connection)
    #         out.add(connection)
    #     current_degree += 1
    # print("Out",out,"Length",len(out))
    # print(final_path)
    # if center in out:
    #     out.remove(center)
    # out = set()
    # for a in final_actors:
    #     if a!=center:
    #         out.add(a)
    print(sorted(set(agenda)))
    return set(current_actors)


def bacon_path(transformed_data, actor_id):
    transformed_data=transform_data(transformed_data)
    center=4724
    output = [(center,)]
    visited = set()
    final_path=None
    #this_path=[]
    while output:
        this_path=output.pop(0)
        terminal_state=this_path[-1]

        #print(this_path,end=' ')
        #terminal_state=output[-1]
        #this_path.append(terminal_state)
        if terminal_state==actor_id:
             final_path=this_path
             break
        connections = transformed_data[terminal_state]
        for conn,_ in connections:
            if conn in visited:
                continue
            new_path = this_path+(conn,)

            visited.add(conn)
            output.append(new_path)
    return set(final_path)



def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    transformed_data=transform_data(transformed_data)
    agenda = [actor_id_1]
    visited = {actor_id_1}
    paths = []



def actor_path(transformed_data, actor_id_1, goal_test_function):
    raise NotImplementedError("Implement me!")


def actors_connecting_films(transformed_data, film1, film2):
    raise NotImplementedError("Implement me!")


if __name__ == "__main__":
    with open("resources/small.pickle", "rb") as f:
        smalldb = pickle.load(f)

    with open('resources/tiny.pickle',"rb") as f:
        tiny_data = pickle.load(f)

    expected = {
        1640,
        1811,
        2115,
        2283,
        2561,
        2878,
        3085,
        4025,
        4252,
        4765,
        6541,
        9827,
        11317,
        14104,
        16927,
        16935,
        19225,
        33668,
        66785,
        90659,
        183201,
        550521,
        1059002,
        1059003,
        1059004,
        1059005,
        1059006,
        1059007,
        1232763,
    }
    # print(tiny_data)
    # print(acted_together(tiny_data,4724,1640))
    #print(actors_with_bacon_number(tiny_data, 0))
    data = {}
    for actor1, actor2,film in tiny_data:
        data.setdefault(actor1,set()).add((actor2,film))
        data.setdefault(actor2,set()).add((actor1,film))

    print(data)
    a=len(transform_data(smalldb)[4724])
    print(a)
    bacon_id_0 =  {x for x,y in data[4724]}
    center = 4724
    for actor,_ in data[4724]:
        bacon_id_0.add(actor)
    # print(bacon_id_0)

    actors_2=actors_with_bacon_number(transform_data(smalldb),2)
    print(sorted(actors_2))
    print(len(actors_2.intersection(expected)))
    print("Actors:",sorted(actors_2))
    print("Expected:",sorted(expected))
    # print(len(expected))
    # print(len(actors_2))
    #
    # print(bacon_path(transform_data(smalldb),46866))
