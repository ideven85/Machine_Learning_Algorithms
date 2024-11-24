GRID_SIZE = 3

def load_words(length):
    file = 'all_words.txt'
    with open(file,'r') as f:
        return [w for w in f.read().split('\n') if len(w)==length]


WORDS = load_words(length=GRID_SIZE)  # list of English words of given length
#print(WORDS)

def format_data(grid_size):
    """
    Builds a data structure containing three mappings:
    slot_to_word: Holds the eventual solution to the puzzle, which maps each slot like
    (2, "down") or (3, "across") to a word. Initially, these are all None.
    slot_to_cells: For each slot, contains a list of cells the slot occupies, along
    with their offset (letter index) into the solution.
    For example: (0, "down"): [((0, 0), 0), ((1, 0), 1), ((2, 0), 2)],
    means slot "0 down" has its 0-th letter at (0,0), its 1-st letter at
    (1,0), and its letter 2 at (2, 0).
    cell_to_slots: For each cell, contains a list of the slots that cross that slot.
    For example, (0, 1): [((0, "across"), 1), ((1, "down"), 0)] means
    that cell (0, 1) is a part of "0 across" (holding its letter 1)
    and "1 down" (holding its letter 0).
    >>> format_data(3)

        {'slot_to_word': {(0, 'across'): None, (0, 'down'): None, (1, 'across'): None,
        (1, 'down'): None, (2, 'across'): None, (2, 'down'): None},
        'slot_to_cells': {(0, 'across'): [((0, 0), 0), ((0, 1), 1), ((0, 2), 2)],
        (0, 'down'): [((0, 0), 0), ((1, 0), 1), ((2, 0), 2)],
        (1, 'across'): [((1, 0), 0), ((1, 1), 1), ((1, 2), 2)],
        (1, 'down'): [((0, 1), 0), ((1, 1), 1), ((2, 1), 2)],
        (2, 'across'): [((2, 0), 0), ((2, 1), 1), ((2, 2), 2)],
        (2, 'down'): [((0, 2), 0), ((1, 2), 1), ((2, 2), 2)]},
        'cell_to_slots': {(0, 0): [((0, 'across'), 0), ((0, 'down'), 0)],
        (0, 1): [((0, 'across'), 1), ((1, 'down'), 0)],
        (0, 2): [((0, 'across'), 2), ((2, 'down'), 0)],
        (1, 0): [((1, 'across'), 0), ((0, 'down'), 1)],
        (1, 1): [((1, 'across'), 1), ((1, 'down'), 1)],
        (1, 2): [((1, 'across'), 2), ((2, 'down'), 1)],
        (2, 0): [((2, 'across'), 0), ((0, 'down'), 2)],
        (2, 1): [((2, 'across'), 1), ((1, 'down'), 2)],
        (2, 2): [((2, 'across'), 2), ((2, 'down'), 2)]}}
    """
    slot_to_word= {(0, 'across'): None, (0, 'down'): None, (1, 'across'): None,
                     (1, 'down'): None, (2, 'across'): None, (2, 'down'): None}

    slot_to_cells= {(0, 'across'): [((0, 0), 0), ((0, 1), 1), ((0, 2), 2)],
                      (0, 'down'): [((0, 0), 0), ((1, 0), 1), ((2, 0), 2)],
                      (1, 'across'): [((1, 0), 0), ((1, 1), 1), ((1, 2), 2)],
                      (1, 'down'): [((0, 1), 0), ((1, 1), 1), ((2, 1), 2)],
                      (2, 'across'): [((2, 0), 0), ((2, 1), 1), ((2, 2), 2)],
                      (2, 'down'): [((0, 2), 0), ((1, 2), 1), ((2, 2), 2)]},
    cell_to_slots= {(0, 0): [((0, 'across'), 0), ((0, 'down'), 0)],
                      (0, 1): [((0, 'across'), 1), ((1, 'down'), 0)],
                      (0, 2): [((0, 'across'), 2), ((2, 'down'), 0)],
                      (1, 0): [((1, 'across'), 0), ((0, 'down'), 1)],
                      (1, 1): [((1, 'across'), 1), ((1, 'down'), 1)],
                      (1, 2): [((1, 'across'), 2), ((2, 'down'), 1)],
                      (2, 0): [((2, 'across'), 0), ((0, 'down'), 2)],
                      (2, 1): [((2, 'across'), 1), ((1, 'down'), 2)],
                      (2, 2): [((2, 'across'), 2), ((2, 'down'), 2)]}
    return {"slot_to_word":slot_to_word,"slot_to_cells":slot_to_cells,"cell_to_slots":cell_to_slots}


def solve(puzzle):
    """Given a partially completed puzzle (in the format returned by
    format_data), fills in the rest of the values."""
    if all(v is not None for v in puzzle["slot_to_word"].values()):
        yield puzzle
        return
    next_slot = next(
        slot for slot, slot_value in puzzle["slot_to_word"].items()
        if slot_value is None
    )
    for word in WORDS:
        new_puzzle = update_puzzle(puzzle, next_slot, word)
        for solved_puzzle in solve(new_puzzle):
            if check_puzzle(solved_puzzle, next_slot):
                yield solved_puzzle


def update_puzzle(puzzle, slot, word):
    """Return a new puzzle with word in the given slot"""
    new_puzzle = {k: v.copy() for k, v in puzzle.items()}
    new_puzzle["slot_to_word"][slot] = word
    return new_puzzle


def check_puzzle(puzzle, slot):
    """For a given slot, return True if the word in that slot does not
    conflict with any letters in any other slots filled in so far."""
    my_word = puzzle["slot_to_word"][slot]
    for cell, offset in puzzle["slot_to_cells"][slot]:
        my_letter = my_word[offset]
        for other_slot, other_offset in puzzle["cell_to_slots"][cell]:
            if other_slot == slot:
                continue
            other_word = puzzle["slot_to_word"][other_slot]
            if other_word is None or other_word[other_offset] == my_letter:
                continue
            else:
                return False
    return True

def main():
    puzzle = load_words(format_data(3))
    solutions = solve(puzzle)
    for _ in range(10):
        print_solution(next(solutions))