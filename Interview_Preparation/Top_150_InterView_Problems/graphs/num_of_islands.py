def num_of_islands(grid):

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < columns and grid[r][c] == "1"

    def dfs(current_row, current_column):
        for dx, dy in directions:
            next_row, next_col = current_row + dx, current_column + dy
            if is_valid(next_row, next_col) and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                dfs(next_row, next_col)

    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    ans = 0
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == "1" and (row, col) not in visited:
                ans += 1

                visited.add((row, col))
                dfs(row, col)
            print(visited)
    return ans


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(num_of_islands(grid))
