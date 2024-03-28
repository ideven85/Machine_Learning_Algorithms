"""
Question 2: Assuming that transformed_data was a list of
(actor_id_1, actor_id_2, film_id) tuples, write the body of the
get_neighbors function below.

You may test your function by running `pytest -v q2_neighbors.py`
(no quotes) in your terminal.
"""


def get_neighbors(transformed_data, actor):
    """
    Gets a set of all of the actors that the provided actor id
    has acted with (not including the given actor).
    """


def test_get_neighbors():
    tiny_db = [
        (2876, 4724, 617),
        (4724, 1532, 31932),
        (1532, 1532, 31932),
        (1532, 4724, 617),
        (1532, 2876, 31932),
        (2876, 1640, 617),
        (1640, 1640, 74881)
    ]

    def check(actor, expected):
        # an example of a useful closure function!
        result = get_neighbors(tiny_db, actor)
        assert result == expected, f"unexpected result for actor {actor}\n {result=} != {expected=}"

    check(2876, {4724, 1532, 1640})
    check(4724, {2876, 1532})
    check(1532, {2876, 4724})
    check(1640, {2876})
    check(1, set())
    print("all correct!")