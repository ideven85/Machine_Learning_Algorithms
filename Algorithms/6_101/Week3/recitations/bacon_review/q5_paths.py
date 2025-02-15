"""
Question 5: Given the following outlines of different path finding
functions below, discuss:
- what's good about these functions?
- what could be improved?
- is there anything potentially buggy in these solutions?
"""


def bacon_path(transformed_data, actor_id):
    """
    bacon path
    """
    agenda = [(4724,)]
    visited = [(4724,)]
    ...  # 20 lines of path-finding code from reading, using actor_id as the goal


def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    """
    Given a database from transform_data(),
    return a shortest path of actors from actor 1 to actor 2 as a list.
    """
    agenda = [(actor_id_1,)]
    visited = [(actor_id_1,)]
    ...  # same 20 lines of path-finding code from reading, using actor_id_2 as the goal


def actor_path(transformed_data, actor_id_1, goal_test_function):
    """
    Given a database from transform_data(),
    return a shortest path of actors starting from actor 1 until reaching an actor who
    satisfies goal_test_function (which takes an actor and returns a truthy value).
    """
    ...  # path-finding code using actor_id_1 as start and goal_test_function(actor) as the stopping criterion
