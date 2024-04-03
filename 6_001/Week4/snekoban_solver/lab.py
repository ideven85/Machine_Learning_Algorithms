"""
6.1010 Lab 4:
Snekoban Game
"""

import json
import typing

# NO ADDITIONAL IMPORTS!
from collections import defaultdict


def find_path(graph, start, goal_test):
    if goal_test(start):
        return (start,)
    agenda = [(start,)]
    visited = {start}
    while visited:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]  # Means?

        for neighbour in graph.get(terminal_state, []):
            if neighbour not in visited:
                new_path = this_path + (neighbour,)

                if goal_test(neighbour):
                    return this_path
                agenda.append(new_path)
                visited.add(neighbour)

    return None


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}


def make_new_game(level_description):
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions.
    """
    game_state = defaultdict(set)
    # game_state = {'wall': (), 'player': (), 'computer':(), 'target': ()}
    n = len(level_description)
    for i in range(n):
        for j in range(len(level_description[i])):
            cell = level_description[i][j]
            if not cell:
                game_state["empty"].add((i, j))
            for k in range(len(cell)):
                game_state[cell[k]].add((i, j))

    return game_state


def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """
    game = make_new_game(game)
    # print(game)
    return game["computer"] == game["target"]


def step_game(game, direction):
    """
    Given a game representation (of the form returned from make_new_game),
    return a new game representation (of that same form), representing the
    updated game after running one step of the game.  The user's input is given
    by direction, which is one of the following:
        {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    raise NotImplementedError


def dump_game(game):
    """
    Given a game representation (of the form returned from make_new_game),
    convert it back into a level description that would be a suitable input to
    make_new_game (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """
    game_state = make_new_game(game)
    level_description = []
    states = sorted(
        list(
            set(
                (
                    list(game_state["empty"])
                    + list(game_state["wall"])
                    + list(game_state["computer"])
                    + list(game_state["target"])
                    + list(game_state["player"])
                )
            )
        )
    )

    level_description.append(states)
    return level_description


def solve_puzzle(game):
    """
    Given a game representation (of the form returned from make_new_game), find
    a solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """
    game_state = make_new_game(game)
    agenda = game_state["player"]
    raise NotImplementedError


if __name__ == "__main__":
    l = [
        [[], ["wall"], ["computer"]],
        [["target", "player"], ["computer"], ["target"]],
    ]
    game_state = make_new_game(l)
    print(game_state)
    print(victory_check(l))
    print(dump_game(l))
