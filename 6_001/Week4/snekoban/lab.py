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

player_position = None
def make_new_game(level_description):
    global player_position
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
    #print(level_description)
    if player_position:
        level_description[player_position[0]][player_position[1]] = 'player'
        return level_description
    game = dict()
    k = len(level_description)*len(level_description[0])
    o=0
    rows = len(level_description[0])
    columns = len(level_description)
    for row in range(rows):
        for col in range(columns):
            if level_description[row][col] and level_description[row][col] == ['player']:
                player_position = (row, col)
                print(player_position[0])
                print(player_position[1])
                level_description[row][col]='player'

    print(game)
    return level_description


def victory_check(game):
    """
    Given a game representation (of the form returned from make_new_game),
    return a Boolean: True if the given game satisfies the victory condition,
    and False otherwise.
    """
    pass


def is_valid_move(game,direction):
    global player_position
    position  = (player_position[0]+direction[0],player_position[1]+direction[1])
    height = len(game[0])
    width = len(game)
    if position[0] <= 0 or position[1] <= 0 or position[1] >= height-1 or position[0] >= width-1 or game[position[0]][position[1]] == ['wall'] :
        return False
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

    if is_valid_move(game, direction_vector[direction]):
        game[player_position[0]][player_position[1]] = []
        player_position[0]=player_position[0]+direction_vector[direction][0]
        player_position[1]=player_position[1]+direction_vector[direction][1]
        game[player_position[0]][player_position[1]]='player'
        return make_new_game(game)

    #         if direction == 'up':
            #
            #             if is_valid_move(game,game[i][j+1],position):
            #                 game[i][j]=''
            #                 game[i+1][j]='player'
            #
            #
            #         elif direction == 'down':
            #
            #                if is_valid_move(game,game[i][j-1],position):
            #                    game[i][j]=''
            #                    game[i][j-1]='player'
            #                    flag = True
            #                    break
            #
            #         elif direction == 'left':
            #
            #                if is_valid_move(game,game[i][j-1],position):
            #                    game[i][j]=''
            #                    game[i-1][j]='player'
            #
            #
            #         elif direction == 'right':
            #             if is_valid_move(game, game[i][j], position):
            #                 game[i][j] = ''
            #                 game[i+1][j] = 'player'
            #     flag = True
            #     break
            # if flag:
            #     break
            #

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
    row=player_position[0]
    column=player_position[1]
    game[row][column]='player'
    return game



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
