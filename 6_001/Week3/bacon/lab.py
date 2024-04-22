"""
6.101 Lab 3:
Bacon Number
"""
import copy

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

# Done and correct
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



#todo Implement This Date_Started 21st April Actually Tougher than any
"""
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
"""
# def actors_with_bacon_number(transformed_data, n):
#     """
#     n is the smallest number of films separating the actors from center 4724
#     """
#
#     #Redo
#     def dfs_for_bacon_ids(actor, visited_actors,visited_films, current_degree, current_actors):
#         # print(current_actors,end=' ')
#         if current_degree>n:
#             return True
#
#
#         connections= acted_together_data[actor]
#         if not connections:
#             return False
#         #print(connections)
#         for conn,film in connections:
#             if conn in visited_actors:
#                 continue
#             # if film in visited_films:
#             #     return dfs_for_bacon_ids(actor,visited_actors,visited_films,current_degree-1,current_actors)
#             visited_actors.add(conn)
#             visited_films.add(film)
#             current_actors.add(conn)
#             if dfs_for_bacon_ids(conn, visited_actors,visited_films, current_degree+1, current_actors):
#                 return True
#
#         return False
#     acted_together_data = transform_data(transformed_data)
#
#     center=4724
#
#     current_degree = 0
#     agenda = 4724
#     out=[0 for _ in range(n+1)]
#     visited_actors=set()
#     visited_films = set()
#     current_actors=set()
#     while current_degree!=n+1:
#
#         if dfs_for_bacon_ids(agenda,visited_actors,visited_films,current_degree,current_actors):
#             print(current_actors,current_degree)
#
#
#         #current_actors=[]
#
#         current_degree+=1
#     final_actors = []
#     visited_actors = set()
#
#     #print(output)
#
#     #print(visited_films)
#
#     return set(current_actors)


def actors_with_bacon_number(transformed_data,n):
    transformed_data=transform_data(transformed_data)
    center=4724
    start=transformed_data[center]
    actors_0={actor for actor,_ in start}
    out = [None for _ in range(n+1)]
    degree=0
    actors_current = None
    visited = set()
    for i in range(n+1):
        if i==0:
            # visited|=actors_0
            out[0]=actors_0
            continue
        actors_current=[center]
        current=set()
        print(current)
        while actors_current:
            current_actor = actors_current.pop(0)
            connections = transformed_data[current_actor]
            if not connections:
                continue
            for conn,_ in connections:
                if conn in visited:
                    continue
                visited.add(conn)
                current.add(conn)
                actors_current.append(conn)
        out[i]=list(copy.deepcopy(current))
        current.clear()
    print(sorted(visited))
    for i  in range(len(out)):
        print(i,sorted(list(out[i])))
    return out[n-1]









# Done And Correct
def bacon_path(transformed_data, actor_id):
    final_path = actor_to_actor_path(transformed_data,4724,actor_id)
    return list(final_path) if final_path else None




# Done And Correct
def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    transformed_data=transform_data(transformed_data)
    agenda = [(actor_id_1,)]
    visited = {actor_id_1}
    final_path=None
    while agenda:
        this_path=agenda.pop(0)
        terminal_state = this_path[-1]
        if terminal_state==actor_id_2:
            final_path=this_path
            break

        connections = transformed_data.get(terminal_state,[])
        for conn,_ in connections:
            if conn in visited:
                continue
            visited.add(conn)
            new_path=this_path+(conn,)
            agenda.append(new_path)
    return final_path


# Done And Correct
def movie_path(data,actor_id1,actor_id2):
    """
    Given two actors return a sequence of movie names which connect first actor
    to the second actor
    """
    #data=transform_data(data)

    actors = actor_to_actor_path(data,actor_id1,actor_id2)
    movie_mapping = dict()
    with open('resources/movies.pickle', 'rb') as f:
        movies = pickle.load(f)
    for movie_name, movie_id in movies.items():
        movie_mapping[movie_id] = movie_name
    new_data = dict()
    for actor1, actor2,film in data:
        movie_name=movie_mapping[film]
        new_data.setdefault(actor1,set()).add(movie_name)
        new_data.setdefault(actor2,set()).add(movie_name)
    movie_names = set()
    for actor in actors:
        movie=new_data[actor]
        for x in movie:
            movie_names.add(x)
    return movie_names

# We can use this function instead of repeatedly writing the same code
def actor_path(transformed_data, actor_id_1, goal_test_function):
   graph=transform_data(transformed_data)

   if goal_test_function(actor_id_1):
        return [actor_id_1]
   out = list()
   agenda = [(actor_id_1,)]
   visited = {actor_id_1}
   while agenda:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]


        connections = transformed_data.get(terminal_state,[])
        for conn, _ in connections:
            if conn in visited:
                continue
            visited.add(conn)

            if goal_test_function(conn):
                    return list(this_path)
            new_path = this_path + (conn,)
            agenda.append(new_path)

            agenda.append(new_path)
            visited.add(conn)

   return None



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

    # print(data)
    actors_0=set()
    a=transform_data(smalldb)[4724]
    for actor,_ in a:
        if actor in expected:
            print("Yes")
        actors_0.add(actor)
    print(sorted(actors_0))
    #bacon_id_0 =  {x for x,y in data[4724]}
    # center = 4724
    # for actor,_ in data[4724]:
    #     bacon_id_0.add(actor)
    # print(bacon_id_0)
    n=2
    actors_2=actors_with_bacon_number(transform_data(smalldb),n)
    print("Actors: Wirth Bacon Nunber:",n,sorted(set(actors_2)))
    # print(len(actors_2.intersection(expected)))
    # print("Actors:",sorted(actors_2))
    print("Expected:",sorted(expected))
    # print(len(expected))
    # print(len(actors_2))
    #
    # print(bacon_path(transform_data(smalldb),46866))
    print(actor_to_actor_path(transform_data(smalldb),4724,1640))

    print(movie_path(tiny_data,4724,2876))
    movie_mapping = dict()
    with open('resources/movies.pickle', 'rb') as f:
        movies = pickle.load(f)
    for movie_name, movie_id in movies.items():
        movie_mapping[movie_id] = movie_name