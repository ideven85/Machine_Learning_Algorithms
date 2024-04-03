"""
6.1010 Lab 4:
Snekoban Game
"""

import json
import typing
from collections import defaultdict

# NO ADDITIONAL IMPORTS!


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}
board_pieces = ["wall", "player", "computer", "target"]
player_position = None


def make_new_game(level_description):
    global player_position
    g = level_description[:]
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
    print(level_description)
    # level_description=level_description[1:-1]
    game = dict()
    player_position = [
        (r, c)
        for r in range(len(level_description))
        for c in range(len(level_description[r]))
        if "player" in level_description[r][c]
    ][0]
    print(player_position)

    return level_description


def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """
    game = make_new_game(game)
    for i in range(len(game)):
        for j in range(len(game[i])):
            if "target" in game[i][j] and "computer" not in game[i][j]:
                return False
    first = "target"
    second = "computer"

    return True


def is_valid_move(game, row, col, direction):
    global player_position
    # row,col = player_position
    print(row, col)
    position = (row + direction[0], col + direction[1])
    height = len(game)
    width = len(game[0])
    print(position)
    if (
        position[0] < 0
        or position[1] < 0
        or position[0] >= height
        or position[1] >= width
        or "wall" in game[position[0]][position[1]]
    ):
        return False
    if "computer" in game[position[0]][position[1]]:
        if is_valid_move_helper(game, position[0], position[1], direction):
            step_game_helper(game, position[0], position[1], direction)
        else:
            return False

            # We are moving computer in the same direction,
    #       # so if the cell is empty we have to make a helper function like step_game again with computer
    player_position = position
    return True


def is_valid_move_helper(game, row, column, direction):
    position = (row + direction[0], column + direction[1])
    height = len(game)
    width = len(game[0])
    print(position)
    if (
        position[0] < 0
        or position[1] < 0
        or position[0] >= height
        or position[1] >= width
        or "wall" in game[position[0]][position[1]]
        or "computer" in game[position[0]][position[1]]
    ):
        return False
    # player_position=position
    return True


def step_game(game, direction):
    global player_position
    """
    Given a game representation (of the form returned from make_new_game),
    return a new game representation (of that same form), representing the
    updated game after running one step of the game.  The user's input is given
    by direction, which is one of the following:
        {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    game = make_new_game(game)
    row, col = player_position
    print(direction_vector[direction])
    if is_valid_move(game, row, col, direction_vector[direction]):

        game[row][col].remove("player")
        potential_row, potential_col = (
            row + direction_vector[direction][0],
            col + direction_vector[direction][1],
        )
        # player_position[1] = player_position[1] + direction_vector[direction][1]
        # game[player_position[0]][player_position[1]].append("player")

        game[potential_row][potential_col].append("player")
        player_position = (potential_row, potential_col)
        return make_new_game(game)
    else:
        return make_new_game(game)


def step_game_helper(game, row, column, direction):
    game[row][column].remove("computer")
    next_row, next_column = row + direction[0], column + direction[1]
    game[next_row][next_column].append("computer")
    return make_new_game(game)


def dump_game(game):
    global player_position

    """
    Given a game representation (of the form returned from make_new_game),
    convert it back into a level description that would be a suitable input to
    make_new_game (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """
    game = make_new_game(game)
    # row = player_position[0]
    # column = player_position[1]
    # game[row][column] = ["player"]
    return game


# todo Estimated time to do: 3 hours
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
    game = [
        [["wall"], [], [], [], [], [], ["wall"]],
        [["wall"], [], [], [], [], [], ["wall"]],
        [["wall"], [], ["target"], ["computer"], ["player"], [], ["wall"]],
        [["wall"], [], [], [], [], [], ["wall"]],
        [["wall"], [], [], [], [], [], ["wall"]],
    ]
    # w = len(level1[0])
    # h=len(level1)
    # print(level1[h-1][0][1])
    # with open('puzzles/m1_001.json','rb') as f:
    #     game = json.load(f)

    #
    # print(game)
    game = make_new_game(game)
    print("Starting Player Position:", player_position)
    step_game(game, "left")
    print("After Moving Left: ", player_position)
    print("Current Status: ", game)
    step_game(game, "left")
    print("Left:", player_position[0], player_position[1])
