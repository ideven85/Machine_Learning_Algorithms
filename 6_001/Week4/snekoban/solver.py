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
rows = [0]
columns = [0]
game_state = defaultdict(list)


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
    # print(level_description)
    # level_description=level_description[1:-1]
    # game = dict()
    # player_position = [
    #     (r, c)
    #     for r in range(len(level_description))
    #     for c in range(len(level_description[r]))
    #     if "player" in level_description[r][c]
    # ][0]
    # print(player_position)
    rows[0] = len(level_description)
    columns[0] = rows[0]
    for i in range(len(level_description)):

        for j in range(len(level_description[i])):

            for val in level_description[i][j]:
                game_state[val].append((i, j))
    # print(game_state['player'][0])

    return game_state


def victory_check(game):
    global game_state
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """
    if not game_state:
        game_state = make_new_game(game)
    print(sorted(game_state["target"]))
    print(sorted(game_state["computer"]))
    return sorted(game_state["target"]) == sorted(game_state["computer"])

    # game_state=make_new_game(game)
    # return


# def is_valid_move(game, row, col, direction):
#     global player_position
#     # row,col = player_position
#     print(row, col)
#     position = (row + direction[0], col + direction[1])
#     height = len(game)
#     width = len(game[0])
#     print(position)
#     if (
#         position[0] < 0
#         or position[1] < 0
#         or position[0] >= height
#         or position[1] >= width
#         or "wall" in game[position[0]][position[1]]
#     ):
#         return False
#     if "computer" in game[position[0]][position[1]]:
#         if is_valid_move_helper(game, position[0], position[1], direction):
#             step_game_helper(game, position[0], position[1], direction)
#         else:
#             return False
#
#             # We are moving computer in the same direction,
#     #       # so if the cell is empty we have to make a helper function like step_game again with computer
#     player_position = position
#     return True
#


def is_valid_move_helper(row, column, direction):
    new_position = (
        row + direction_vector[direction][0],
        column + direction_vector[direction][1],
    )
    if new_position in game_state["wall"] or new_position in game_state["computer"]:
        return False

    game_state["computer"].remove((row, column))
    game_state["computer"].append(new_position)
    print("Hi")
    return True


def step_game(game, direction):
    global game_state
    """
    
        Move the player in the direction pressed by the arrow key
        if the new position is wall or potentially illegal return the same game state
        or else update the game state to reflect the changes
    Args:
        game (): _description_
        direction (_type_): _description_

    Returns:
        _type_: dict(set)
    """
    if not game_state:
        game_state = make_new_game(game)
    print(game_state)
    player_position = game_state["player"][0]
    print(player_position)
    potential_position = (
        player_position[0] + direction_vector[direction][0],
        player_position[1] + direction_vector[direction][1],
    )
    print(potential_position)
    if potential_position in game_state["wall"]:
        return make_new_game(game_state)
    elif potential_position in game_state["computer"]:
        if is_valid_move_helper(*potential_position, direction=direction):
            game_state["player"].remove(player_position)
            game_state["player"].append(potential_position)
            return make_new_game(game_state)
    else:
        game_state["player"].remove(player_position)
        game_state["player"].append(potential_position)

        return make_new_game(game_state)


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
    global rows, columns

    global game_state
    if not game_state:
        game_state = make_new_game(game)
    # print(rows, columns)
    game = [[[] for _ in range(rows[0] + 2)] for _ in range(columns[0] + 1)]

    # print(game)
    walls = game_state["wall"]
    # print(walls[0])
    target = game_state["target"]
    player = game_state["player"]
    computer = game_state["computer"]
    for row, col in walls:
        game[row][col] = ["wall"]
    for row, col in target:
        game[row][col] = ["target"]
    for row, col in player:
        game[row][col] = ["player"]
    for row, col in computer:
        game[row][col] = ["computer"]

    # print(game)
    return game


def solve_puzzle(game):

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
    print(game)
    # print("Starting Player Position:", game['player'])
    # step_game(game, "left")
    # print("After Moving Left: ", player_position)
    # print("Current Status: ", game)
    # game=step_game(game, "left")
    g = dump_game(game)
    print(g)
    # print("Left:", player_position[0], player_position[1])
    # print(game)
