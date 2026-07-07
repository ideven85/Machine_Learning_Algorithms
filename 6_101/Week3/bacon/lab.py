#!/usr/bin/env python3

import pickle

# NO ADDITIONAL IMPORTS ALLOWED!


def transform_data(raw_data):
    """
    Transforms raw list tuples into an optimized adjacency list graph dictionary.
    Keys are Actor IDs, values are sets of (Neighbor Actor ID, Movie ID) tuples.
    """
    data = dict()
    if isinstance(raw_data, list):
        for actor1, actor2, film in raw_data:
            data.setdefault(actor1, set()).add((actor2, film))
            data.setdefault(actor2, set()).add((actor1, film))
        return data
    return raw_data


def acted_together(transformed_data, actor_id_1, actor_id_2):
    """
    Returns True if actor_id_1 and actor_id_2 acted in the same movie.
    Expects transformed_data to ALREADY be optimized by transform_data().
    """
    if actor_id_1 == actor_id_2:
        return True

    if actor_id_1 not in transformed_data:
        return False

    # Check if neighbor target ID exists in the immediate adjacency set
    for neighbor, _ in transformed_data[actor_id_1]:
        if neighbor == actor_id_2:
            return True

    return False


def actors_with_bacon_number(transformed_data, n):
    """
    Returns a set of all actor IDs whose Bacon Number is exactly n using standard BFS.
    """
    center = 4724
    if n == 0:
        return {center}

    if center not in transformed_data:
        return set()

    # Track distances cleanly to lock absolute shortest path values
    distances = {center: 0}
    agenda = [center]

    while agenda:
        current_actor = agenda.pop(0)
        current_dist = distances[current_actor]

        # Optimization stop: we've passed depth n, no need to crawl further
        if current_dist >= n:
            break

        for neighbor, _ in transformed_data.get(current_actor, set()):
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                agenda.append(neighbor)

    return {actor for actor, dist in distances.items() if dist == n}


def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    """
    Finds the shortest sequence of actor IDs connecting actor_id_1 to actor_id_2.
    """
    if actor_id_1 == actor_id_2:
        return [actor_id_1]

    if actor_id_1 not in transformed_data or actor_id_2 not in transformed_data:
        return None

    agenda = [[actor_id_1]]
    visited = {actor_id_1}

    while agenda:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]

        if terminal_state == actor_id_2:
            return this_path

        for neighbor, _ in transformed_data.get(terminal_state, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                agenda.append(this_path + [neighbor])

    return None


def bacon_path(transformed_data, actor_id):
    """
    Traces path starting from Kevin Bacon (4724) to the target actor ID.
    """
    return actor_to_actor_path(transformed_data, 4724, actor_id)


def movie_path(data, actor_id1, actor_id2):
    """
    Given the RAW list data array, tracks the exact sequence of MOVIE IDs
    connecting actor_id1 to actor_id2.
    """
    # 1. First build our graph structure to calculate the node path trace
    transformed = transform_data(data)
    actor_route = actor_to_actor_path(transformed, actor_id1, actor_id2)

    if not actor_route:
        return None

    # 2. Build map pairs to map exactly which movie connects adjacent actors
    movie_route = []
    for i in range(len(actor_route) - 1):
        current_actor = actor_route[i]
        next_actor = actor_route[i + 1]

        # Look up matching movie ID between these two adjacent actors
        for neighbor, movie_id in transformed[current_actor]:
            if neighbor == next_actor:
                movie_route.append(movie_id)
                break

    return movie_route


def actor_path(transformed_data, actor_id_1, goal_test_function):
    """
    Generic BFS graph search evaluating nodes dynamically against a test function.
    """
    if goal_test_function(actor_id_1):
        return [actor_id_1]

    if actor_id_1 not in transformed_data:
        return None

    agenda = [[actor_id_1]]
    visited = {actor_id_1}

    while agenda:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]

        if goal_test_function(terminal_state):
            return this_path

        for neighbor, _ in transformed_data.get(terminal_state, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                agenda.append(this_path + [neighbor])

    return None


def actors_connecting_films(transformed_data, film1, film2):
    """
    Finds and returns a set of all actor IDs who have acted in BOTH film1 and film2.
    """
    actors_in_film1 = set()
    actors_in_film2 = set()

    # Iterate through the adjacency list graph
    for actor_id, connections in transformed_data.items():
        for _, movie_id in connections:
            if movie_id == film1:
                actors_in_film1.add(actor_id)
            if movie_id == film2:
                actors_in_film2.add(actor_id)

    # Return the intersection of both sets (actors present in both films)
    return actors_in_film1 & actors_in_film2
