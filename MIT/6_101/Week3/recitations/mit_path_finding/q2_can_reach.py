"""
Question 2: Fill in the blanks in the can_reach function below.

You can test this function by running `pytest q2_can_reach.py -v`
(without quotes) in the terminal.
"""


def can_reach(map, start_building, goal_building):
    """
    map: dictionary { `building` : set of the directly-connected neighbors of `building` }
    start_building: building to start from
    goal_building: building you're trying to reach

    returns True if and only if you can get from start_building to goal_building through
        directly-connected neighbors, i.e. without going outside
    """

    # helper function to get neighbors of building
    def get_neighbors(building):
        ________

    agenda = [________]  # agenda: buildings still to explore
    visited = {________}  # visited set: all buildings ever added to the agenda

    # while there are still buildings to explore
    while agenda:
        # remove a building from the agenda
        building = ________

        # add each neighbor to agenda
        for neighbor in get_neighbors(building):
            ...

    return _________


# from http://whereis.mit.edu/?zoom=18&lat=42.36162996081668&lng=-71.09057574701308&maptype=mit&open=-1
# (and not using tunnels)
small_map = {
    "26": {"36"},  # 26 connects to 36
    "32": {"36"},  # 32 connects to 36
    "36": {"26", "32"},  # 36 connects to both of the others
    "76": set(),  # Koch building is by itself
}


# why do we have such a small map? why not use the whole campus?
def test_can_reach_small():
    assert can_reach(small_map, "26", "32") is True
    assert can_reach(small_map, "36", "36") is True
    assert can_reach(small_map, "76", "32") is False
