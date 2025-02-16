# 6.101 recitation: lab 7 wrapup
# from solution import new_game_2d
import doctest

############################################ refactoring


def dig_2d(game, row, col):
    """
    Reveal the cell at (row, col), and, in some cases, recursively reveal its
    neighboring squares.

    Update game['visible'] to reveal (row, col).  Then, if (row, col) has no
    adjacent bombs (including diagonally), then recursively reveal (dig up) its
    eight neighbors.  Return an integer indicating how many new squares were
    revealed in total, including neighbors, and neighbors of neighbors, and so
    on.

    The state of the game should be changed to 'defeat' when at least one mine
    is visible on the board after digging (i.e. game['visible'][mine_location]
    == True), 'victory' when all safe squares (squares that do not contain a
    mine) and no bombs are visible, and 'ongoing' otherwise.

    Parameters:
       game (dict): Game state
       row (int): Where to start digging (row)
       col (int): Where to start digging (col)

    Returns:
       int: the number of new squares revealed

    >>> game = new_game_2d(2, 4, [(0,0), (1,0), (1,1)])
    >>> dig_2d(game, 0, 1)
    1
    >>> dig_2d(game, 0, 3)
    4
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    state: victory
    visible:
        [False, True, True, True]
        [False, False, True, True]

    >>> game = new_game_2d(2, 4, [(0,0), (1,0), (1,1)])
    >>> dig_2d(game, 0, 1)
    1
    >>> dig_2d(game, 0, 0)
    1
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    state: defeat
    visible:
        [True, True, False, False]
        [False, False, False, False]
    """
    if game["state"] == "defeat" or game["state"] == "victory":
        game["state"] = game["state"]  # keep the state the same
        return 0

    if game["board"][row][col] == ".":
        game["visible"][row][col] = True
        game["state"] = "defeat"
        return 1

    num_revealed_bombs = 0
    num_revealed_squares = 0
    for r in range(game["dimensions"][0]):
        for c in range(game["dimensions"][1]):
            if game["board"][r][c] == ".":
                if game["visible"][r][c] == True:
                    num_revealed_bombs += 1
            elif game["visible"][r][c] == False:
                num_revealed_squares += 1
    if num_revealed_bombs != 0:
        # if num_revealed_bombs is not equal to zero, set the game state to
        # defeat and return 0
        game["state"] = "defeat"
        return 0
    if num_revealed_squares == 0:
        game["state"] = "victory"
        return 0

    if game["visible"][row][col] != True:
        game["visible"][row][col] = True
        revealed = 1
    else:
        return 0

    if game["board"][row][col] == 0:
        nrows, ncolumns = game["dimensions"]
        if 0 <= row - 1 < nrows:
            if 0 <= col - 1 < ncolumns:
                if game["board"][row - 1][col - 1] != ".":
                    if game["visible"][row - 1][col - 1] == False:
                        revealed += dig_2d(game, row - 1, col - 1)
        if 0 <= row < nrows:
            if 0 <= col - 1 < ncolumns:
                if game["board"][row][col - 1] != ".":
                    if game["visible"][row][col - 1] == False:
                        revealed += dig_2d(game, row, col - 1)
        if 0 <= row + 1 < nrows:
            if 0 <= col - 1 < ncolumns:
                if game["board"][row + 1][col - 1] != ".":
                    if game["visible"][row + 1][col - 1] == False:
                        revealed += dig_2d(game, row + 1, col - 1)
        if 0 <= row - 1 < nrows:
            if 0 <= col < ncolumns:
                if game["board"][row - 1][col] != ".":
                    if game["visible"][row - 1][col] == False:
                        revealed += dig_2d(game, row - 1, col)
        if 0 <= row < nrows:
            if 0 <= col < ncolumns:
                if game["board"][row][col] != ".":
                    if game["visible"][row][col] == False:
                        revealed += dig_2d(game, row, col)
        if 0 <= row + 1 < nrows:
            if 0 <= col < ncolumns:
                if game["board"][row + 1][col] != ".":
                    if game["visible"][row + 1][col] == False:
                        revealed += dig_2d(game, row + 1, col)
        if 0 <= row - 1 < nrows:
            if 0 <= col + 1 < ncolumns:
                if game["board"][row - 1][col + 1] != ".":
                    if game["visible"][row - 1][col + 1] == False:
                        revealed += dig_2d(game, row - 1, col + 1)
        if 0 <= row < nrows:
            if 0 <= col + 1 < ncolumns:
                if game["board"][row][col + 1] != ".":
                    if game["visible"][row][col + 1] == False:
                        revealed += dig_2d(game, row, col + 1)
        if 0 <= row + 1 < nrows:
            if 0 <= col + 1 < ncolumns:
                if game["board"][row + 1][col + 1] != ".":
                    if game["visible"][row + 1][col + 1] == False:
                        revealed += dig_2d(game, row + 1, col + 1)

    num_revealed_bombs = 0  # set number of bombs to 0
    num_revealed_squares = 0
    for r in range(game["dimensions"][0]):
        # for each r,
        for c in range(game["dimensions"][1]):
            # for each c,
            if game["board"][r][c] == ".":
                if game["visible"][r][c] == True:
                    # if the game visible is True, and the board is '.',
                    # add 1 to bombs revealed
                    num_revealed_bombs += 1
            elif game["visible"][r][c] == False:
                num_revealed_squares += 1
    bad_squares = num_revealed_bombs + num_revealed_squares
    if bad_squares > 0:
        game["state"] = "ongoing"
        return revealed
    else:
        game["state"] = "victory"
        return revealed


############################################ refactoring from 2d to n-d


def render_2d_locations(game, all_visible=False):
    """
    Prepare a game for display.

    Returns a two-dimensional array (list of lists) of '_' (hidden squares),
    '.' (bombs), ' ' (empty squares), or '1', '2', etc. (squares neighboring
    bombs).  game['visible'] indicates which squares should be visible.  If
    all_visible is True (the default is False), game['visible'] is ignored
    and all cells are shown.

    Parameters:
       game (dict): Game state
       all_visible (bool): Whether to reveal all tiles or just the ones allowed
                    by game['visible']

    Returns:
       A 2D array (list of lists)

    >>> game = {'dimensions': (2, 4),
    ...         'state': 'ongoing',
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'visible':  [[False, True, True, False],
    ...                   [False, False, True, False]]}
    >>> render_2d_locations(game, False)
    [['_', '3', '1', '_'], ['_', '_', '1', '_']]

    >>> render_2d_locations(game, True)
    [['.', '3', '1', ' '], ['.', '.', '1', ' ']]
    """

    def display(r, c):
        if not all_visible and not game["visible"][r][c]:
            return "_"
        cell = game["board"][r][c]
        if cell == 0:
            return " "
        return str(cell)

    return [
        [display(r, c) for c in range(game["dimensions"][1])]
        for r in range(game["dimensions"][0])
    ]


# def render_nd(game, all_visible=False):
#     """
#     Prepare the game for display.

#     Returns an N-dimensional array (nested lists) of '_' (hidden squares), '.'
#     (bombs), ' ' (empty squares), or '1', '2', etc. (squares neighboring
#     bombs).  The game['visible'] array indicates which squares should be
#     visible.  If all_visible is True (the default is False), the game['visible']
#     array is ignored and all cells are shown.

#     Args:
#        all_visible (bool): Whether to reveal all tiles or just the ones allowed
#                            by game['visible']

#     Returns:
#        An n-dimensional array of strings (nested lists)

#     >>> g = {'dimensions': (2, 4, 2),
#     ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
#     ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
#     ...      'visible': [[[False, False], [False, True], [True, True],
#     ...                [True, True]],
#     ...               [[False, False], [False, False], [True, True],
#     ...                [True, True]]],
#     ...      'state': 'ongoing'}
#     >>> render_nd(g, False)
#     [[['_', '_'], ['_', '3'], ['1', '1'], [' ', ' ']],
#      [['_', '_'], ['_', '_'], ['1', '1'], [' ', ' ']]]

#     >>> render_nd(g, True)
#     [[['3', '.'], ['3', '3'], ['1', '1'], [' ', ' ']],
#      [['.', '3'], ['3', '.'], ['1', '1'], [' ', ' ']]]
#     """
#     raise NotImplementedError


############################################ neighbors in n-d

# def all_n_tuples(elements, n):
#     """
#     given an iterable of elements,
#     returns a list of all possible n-tuples whose elements are drawn from `elements`

#     >>> list(sorted(all_n_tuples([-1,1], 2)))
#     [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     """
#     pass

# def neighbors(x, dimensions):
#     """
#     Returns a list of all the neighbor cells of x in a board with given dimensions.
#     Omits x itself and omits cells that are outside the board.

#     >>> list(sorted(neighbors([1,1], [5,5])))
#     [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
#     >>> list(sorted(neighbors([0,0], [5,5])))
#     [(0, 1), (1, 0), (1, 1)]
#     >>> list(sorted(neighbors([4,4], [5,5])))
#     [(3, 3), (3, 4), (4, 3)]
#     """
#     pass


############################################ boilerplate for doctests


def dump(game):
    """
    Prints a human-readable version of a game (provided as a dictionary)
    """
    keys = ("board", "dimensions", "state", "visible")
    # ^ Uses only default game keys. If you modify this you will need
    # to update the docstrings in other functions!
    for key in keys:
        val = game[key]
        if isinstance(val, list) and val and isinstance(val[0], list):
            print(f"{key}:")
            for inner in val:
                print(f"    {inner}")
        else:
            print(f"{key}:", val)


if __name__ == "__main__":
    # Test with doctests. Helpful to debug individual lab.py functions.
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags, verbose=True)  # runs ALL doctests

    # Alternatively, can run the doctests JUST for specified function/methods,
    # e.g., for render_2d_locations or any other function you might want.  To
    # do so, comment out the above line, and uncomment the below line of code.
    # This may be useful as you write/debug individual doctests or functions.
    # Also, the verbose flag can be set to True to see all test results,
    # including those that pass.
    #
    # doctest.run_docstring_examples(
    #    render_2d_locations,
    #    globals(),
    #    optionflags=_doctest_flags,
    #    verbose=False
    # )
