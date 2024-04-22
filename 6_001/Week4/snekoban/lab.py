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

    rows[0] = len(level_description)
    columns = []
    print(rows,columns)
    i=0;j=0
    for i in range(len(level_description)):
        columns.append(len(level_description[i]))
        for j in range(len(level_description[i])):

            for val in level_description[i][j]:
                if not val:
                    game_state["empty"].append((i, j))
                else:
                    game_state[val].append((i, j))
    #print(game_state["player"][0])

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


def is_valid_move(game, row, col, direction):

    # row,col = player_position
    #print(row, col)
    #print(row,col)
    #print(direction)
    print()
    position = (row+direction_vector[direction][0],col+direction_vector[direction][1])
    print("Player new is valid:",game[position])

    #input()
    #print(position,end=' ')
    if "wall" in game[position]:
        print("Wall",game[position])
        make_new_game(game)
        return False
    if "computer" in game[position]:

           if is_valid_move_helper(game,position[0], position[1], direction):

               print(game['player'])
               game['player']=[]

               game['player'].append((position[0],position[1]))
               make_new_game(game_state)

               return True

    game['player']=[]
    game['player'].append((position[0],position[1]))
    make_new_game(game)
    return True




def is_valid_move_helper(game_state,row, column, direction):
    new_position = (
        row + direction_vector[direction][0],
        column + direction_vector[direction][1],
    )
    #input("What?")
    if new_position in game_state["wall"] or new_position in game_state["computer"]:
        make_new_game(game_state)
        return False

    game_state["computer"].remove((row, column))
    game_state["computer"].append((new_position[0],new_position[1]))
    make_new_game(game_state)
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
        if is_valid_move_helper(game_state,potential_position[0],potential_position[1], direction=direction):
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

    rows1=len(game);columns1=len(game)
    print(rows1,columns1)
    print(rows,columns)
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
    empty = game_state["empty"]

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





# todo {}
def solve_puzzle(game):



    global rows,columns
    # goal=game_state['target']
    # computer = game_state['computer']
    player_position= game['player']
    start=player_position
    print("S:",start)
    #input()
    # empty_positions = game_state['empty']
    visited = set()
    visited.add(player_position[0])

    agenda = start


    def get_neighbours(board,*position):
        positions = []

        for move in direction_vector.keys():
            #print(move,end=' ')
            if is_valid_move(board,position[0],position[1],move):

                #input()

                positions.append((position[0]+direction_vector[move][0],position[1]+direction_vector[move][1]))
       # print("In neighbour positions",positions)
        return positions


    def bfsUtil(board,path):
        while sorted(board['target'])!=sorted(board['computer']):
            print("First",board['player'])
            row,col=path.pop(0)
            if row>rows[0] or col>columns[0]:
                print("Breaking")
                break
            print("Path:",row,col)
            print("C",board[(row,col)])
            this_path.append((row,col))
            #print("C",current_position,end=' ')
            #print(visited)
            #board['player']=current_position
            #input()
            #terminal_state = current_position[(len(current_position)-1)]

            #print(terminal_state,end=' ')

            #this_path.append((current_position[0],current_position[1]))
            if victory_check(board):
                print("Over",this_path)
                break

            neighbours= get_neighbours(board,row,col)
            if neighbours is not None:
                for neighbour in neighbours:

                    if neighbour in visited:
                        continue
                    if neighbour in path:
                        continue
                    visited.add(neighbour)
                    path.append(neighbour)
            print(path)


    game_state=make_new_game(game)
    print(player_position)
    this_path = [(player_position[0][0], player_position[0][1])]
    bfsUtil(game_state,player_position)
    print("Visited:",visited)
    print(game_state['computer'])
    print(game_state['target'])
    print(game_state['player'])
    return this_path







# Start by implementing a search function that returns a sequences of game board states,
# and then a separate helper function that takes in that sequence of states and returns a sequence of necessary actions.


if __name__ == "__main__":
    game = [
        [["wall"], [], [], [], [], [], ["wall"]],
        [["wall"], [], [], [], [], [], ["wall"]],
        [["wall"], [], ["target"], ["computer"], [], [], ["wall"]],
        [["wall"], [], ["player"], [], [], [], ["wall"]],
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
    #print(game)
    # print("Starting Player Position:", game['player'])
    # step_game(game, "left")
    # print("After Moving Left: ", player_position)
    # print("Current Status: ", game)
    # game=step_game(game, "left")
    #g = dump_game(game)
    #print(g)
    # print("Left:", player_position[0], player_position[1])
    # print(game)
    print(solve_puzzle(game))
