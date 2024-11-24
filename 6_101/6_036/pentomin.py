def covers(grid_height, grid_width, pentominoes):
    """
    Given a grid of locations and a list of pentominoes, return True if the given
    arrangement of pentominoes completely covers the board, or False otherwise.  The grid
    should be considered covered if every location from (0, 0) through (grid_height-1,
    grid_width-1) has a part of a pentomino in it, no two pentominoes overlap, and no part
    of any of the given pentominoes extends outside the grid.
    Inputs:
        * grid_height is an integer indicating the height of the grid
        * grid_width is an integer indicating the width of the grid
        * pentominoes is a list of (shape, row, column) tuples, where shape is an
          integer index into the SHAPES array, and row and column represent the location
          in the grid where the (0,0) anchor point of the given shape is placed
    """
    success = True
    for row in range(grid_height):
        for col in range(grid_width):
            if not cell_covered_once(row, col, pentominoes):
                success = False
    for p in pentominoes:
        if not in_bounds(grid_height, grid_width, p):
            success = False
    return success


def add_tuples(t1, t2):
    return tuple(i + j for i, j in zip(t1, t2))


def absolute_locations(p):
    shape, row, column = p
    return [add_tuples((row, column), offset) for offset in SHAPES[shape]]


def in_bounds(grid_height, grid_width, p):
    locations = absolute_locations(p)
    for location in locations:
        if not (0 <= location[0] < grid_height and 0 <= location[1] < grid_width):
            return False
    return True


def cell_covered_once(row, col, pentominoes):
    for p1 in pentominoes:
        if (row, col) in absolute_locations(p1):
            others = [p for p in pentominoes if p != p1]
            for p2 in others:
                if (row, col) in absolute_locations(p2):
                    return False
            return True
    return False
