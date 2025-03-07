from typing import List


def valid_board(board, row, col, N):
    # print(board)
    for k in range(len(board)):
        if board[k][col] == N or board[row][k] == N:
            return False
    side = 9
    rs = row - row % side
    cs = col - col % side
    for i in range(side):
        for j in range(side):
            if board[i + rs][j + cs] == N:
                return False
    # print("Hi")
    return True


def values_in_row(board, r):
    out = set()
    for col in range(9):
        if board[r][col]:
            out |= {board[r][col]}

    return out


def values_in_column(board, c):
    # print(board[c])
    out = set()
    k = 0
    for row in range(9):
        if board[row][c] != 0:
            out |= {board[row][c]}
    return out


def values_in_subgrid(board, sr, sc):
    out = set()
    for i in range(sr):
        for j in range(sc):
            if board[sr][sc]:
                out |= {board[sr][sc]}
    return out


def valid_moves(board, row, col):
    return (
        set(range(1, 10))
        - values_in_row(board, row)
        - values_in_row(board, col)
        - values_in_subgrid(board, row // 3, col // 3)
    )


def print_board(board):
    for row in range(10):
        print(board[row])


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                continue
            for trial in valid_moves(board, row, col):
                new_board = [
                    [trial if (r, c) == (row, col) else board[r][c] for c in range(9)]
                    for r in range(9)
                ]
                if valid_board(new_board, row, col, trial):
                    # print(new_board)
                    result = solve_sudoku(new_board)
                    if result is not None:
                        print("Not None")
                        # print_board(new_board)
                        return result

            return None
    return board


if __name__ == "__main__":
    grid1 = [
        [5, 1, 7, 6, 0, 0, 0, 3, 4],
        [2, 8, 9, 0, 0, 4, 0, 0, 0],
        [3, 4, 6, 2, 0, 5, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 3, 8, 0, 0, 6, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 7, 8],
        [7, 0, 3, 4, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    grid2 = [
        [5, 1, 7, 6, 0, 0, 0, 3, 4],
        [0, 8, 9, 0, 0, 4, 0, 0, 0],
        [3, 0, 6, 2, 0, 5, 0, 9, 0],
        [6, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 3, 0, 0, 0, 6, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 7, 8],
        [7, 0, 3, 4, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    grid3 = [
        [0, 0, 1, 0, 0, 9, 0, 0, 3],  # http://www.extremesudoku.info/sudoku.html
        [0, 8, 0, 0, 2, 0, 0, 9, 0],
        [9, 0, 0, 1, 0, 0, 8, 0, 0],
        [1, 0, 0, 5, 0, 0, 4, 0, 0],
        [0, 7, 0, 0, 3, 0, 0, 5, 0],
        [0, 0, 6, 0, 0, 4, 0, 0, 7],
        [0, 0, 8, 0, 0, 5, 0, 0, 6],
        [0, 3, 0, 0, 7, 0, 0, 4, 0],
        [2, 0, 0, 3, 0, 0, 9, 0, 0],
    ]
    grid4 = [
        [3, 8, 5, 0, 0, 0, 0, 0, 0],
        [9, 2, 1, 0, 0, 0, 0, 0, 0],
        [6, 4, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 3, 0, 0, 0],
        [0, 0, 0, 7, 8, 4, 0, 0, 0],
        [0, 0, 0, 6, 9, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 7, 3],
        [0, 0, 0, 0, 0, 0, 9, 6, 2],
        [0, 0, 0, 0, 0, 0, 1, 4, 5],
    ]
    # print(solve_sudoku(grid1))
    # print(solve_sudoku(grid2))
    # print(solve_sudoku(grid4))
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(len(board))
    print(solve_sudoku(grid2))
    print(solve_sudoku(grid1))
    print(solve_sudoku(grid3))
    print(solve_sudoku(grid4))

    print(values_in_column(grid4, 2))
    print(values_in_subgrid(grid4, 3, 3))
