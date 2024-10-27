from collections import defaultdict


def find_path(graph, start, goal_test):
    if goal_test(start):
        return (start,)
    agenda = [(start,)]
    visited = {start}
    while visited:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]  # Means?

        for neighbour in graph.get(terminal_state, []):
            if neighbour not in visited:
                new_path = this_path + (neighbour,)

                if goal_test(neighbour):
                    return this_path
                agenda.append(new_path)
                visited.add(neighbour)

    return None


def findNumberOfProvinces(graph):
    res = 0

    # def dfs(row,column):
    #     if row==n-1 and column==n-1:
    #         return True
    #     if (row,column) in visited:
    #         return False
    #     for neighbour in get_neighbors(row,column):
    #
    #         current_row,current_column = neighbour
    #         if (current_row,current_column) in visited:
    #             continue
    #         visited.add((current_column,current_column))
    #         if graph[current_row][current_column]==1:
    #            if dfs(current_row,current_column):
    #                return True
    #     return False
    #
    # def get_neighbors(row,column):
    #     neighbors = {(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1),
    #                  (row - 1, column - 1), (row + 1, column + 1), (row - 1, column + 1), (row + 1, column - 1)}
    #     return {(nr, nc) for (nr, nc) in neighbors if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited}
    def dfs(node):
        for neighbor in isConnected[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    n = len(graph)
    isConnected = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                isConnected[i].append(j)
                isConnected[j].append(i)

    print(isConnected)
    res = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            visited.add(i)

            res += 1
            dfs(i)
    print(visited)
    return res


if __name__ == "__main__":
    is_connected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(findNumberOfProvinces(is_connected))
    print(findNumberOfProvinces(matrix))
