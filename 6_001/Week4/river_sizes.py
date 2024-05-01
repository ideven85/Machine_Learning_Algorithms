def riverSizes(matrix):
    # Write your code here.
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def dfsUtil(row, column):
        potential_neighbours = [
            (row + dx, column + dy)
            for dx, dy in directions
            if 0 <= (row + dx) < rows
            and 0 <= (column + dy) < curr_column
            and (row + dx, column + dy) not in visited
            and matrix[row + dx][column + dy] == 1
        ]
        if not potential_neighbours:
            return 1
        for r, c in potential_neighbours:
            visited.add((r, c))
            return 1 + dfsUtil(r, c)
        return 1

    visited = set()
    sizes = []
    rows = len(matrix)
    for i in range(len(matrix)):
        curr_column = len(matrix[i])
        for j in range(len(matrix[i])):
            if (i, j) in visited:
                continue
            if matrix[i][j] == 1:
                visited.add((i, j))

                size = dfsUtil(i, j)
                if size:
                    sizes.append(size)
    return sizes


m = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]
print(riverSizes(m))
