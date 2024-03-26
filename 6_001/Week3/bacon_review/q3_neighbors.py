"""
Question 3: Assuming that transformed_data was a dictionary where the keys
were actor_ids and the values were sets of co-star actor_ids, write the body
of the get_neighbors function below.

You may test your function by running `pytest -v q3_neighbors.py`
(no quotes) in your terminal.
"""

from collections import defaultdict


def get_neighbors(transformed_data, actor):
    """
    Gets a set of all of the actors that the provided actor id
    has acted with (not including the given actor).
    """
    db = defaultdict(set)
    if actor in transformed_data:
        for actor_id, acted in transformed_data.items():

            for neighbor in acted:
                if neighbor == actor:
                    continue
                db[actor_id].add(neighbor)
    return db[actor]


def test_get_neighbors():
    tiny_db = {
        2876: {4724, 1532, 1640},
        4724: {2876, 1532},
        1532: {2876, 4724, 1532},
        1640: {2876},
    }

    def check(actor, expected):
        # an example of a useful closure function!
        result = get_neighbors(tiny_db, actor)
        assert (
            result == expected
        ), f"unexpected result for actor {actor}\n {result=} != {expected=}"

    check(2876, {4724, 1532, 1640})
    check(4724, {2876, 1532})
    check(1532, {2876, 4724})
    check(1640, {2876})
    check(1, set())
    print("all correct!")
