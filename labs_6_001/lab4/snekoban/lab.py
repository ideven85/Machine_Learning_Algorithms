"""
6.1010 Lab:
Snekoban Game
"""

import json
import typing

# NO ADDITIONAL IMPORTS!


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}
from collections import defaultdict


def get_rows_and_columns(game):
    rows = len(game)
    columns = len(game[0])
    return rows, columns


def make_new_game(level_description):
    if isinstance(level_description, defaultdict):
        return level_description
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
    # raise NotImplementedError

    rows, columns = get_rows_and_columns(level_description)
    game = defaultdict(list)

    for row in range(rows):
        for col in range(columns):
            # if not level_description[row][col]:
            #     game[row][col]=[]
            # else:
            for x in range(len(level_description[row][col])):
                game[level_description[row][col][x]].append((row, col))
    return game


def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """

    game = make_new_game(game)
    return sorted(game["computer"]) == sorted(game["target"])


def step_game(game, direction):
    """
    Given a game representation (of the form returned from make_new_game),
    return a new game representation (of that same form), representing the
    updated game after running one step of the game.  The user's input is given
    by direction, which is one of the following:
        {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    # raise NotImplementedError
    rows, columns = get_rows_and_columns(game)

    def step_game_helper():
        if (
            0 <= row + dx < rows
            and 0 <= col + dy < columns
            and game[row + dx][col + dy] != "wall"
        ):
            if "computer" in game[row + dx][col + dy]:
                potential_row, potential_col = row + dx + dx, col + dy + dy

                if 0 <= potential_row < rows and 0 <= potential_col < columns:
                    if (
                        "computer" in game[potential_row][potential_col]
                        or "wall" in game[potential_row][potential_col]
                    ):
                        return game
                    else:
                        game[row][col] = []
                        game[row + dx][col + dy].remove("computer")
                        game[row + dx][col + dy].append("player")
                        game[potential_row][potential_col].append("computer")
            else:
                game[row][col] = []
                game[row + dx][col + dy].append("player")
            return game

    game = make_new_game(game)
    dx, dy = direction_vector[direction]
    row, col = game["player"]
    return make_new_game(step_game_helper())


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
    print(game)
    rows, columns = get_rows_and_columns(game)
    game = make_new_game(game)
    out = [[None for _ in range(columns)] for _ in range(rows)]

    return out


def solve_puzzle(game):
    """
    Given a game representation (of the form returned from make_new_game), find
    a solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """
    raise NotImplementedError


if __name__ == "__main__":
    pass
