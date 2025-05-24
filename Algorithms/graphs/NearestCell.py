from collections import deque
from typing import List


# todo
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        if m * n == 0:
            return []
        queue = deque()
        queue.append((0, 0))
        output = mat[:]
        while queue:
            row, col = queue.popleft()
            flag = False

            visited[row][col] = True

            adjacents = self.getAdjacent(mat, row, col, visited)
            for adj in adjacents:
                adjacentRow, adjacentCol = adj
                if visited[adjacentRow][adjacentCol]:
                    continue

                if mat[adjacentRow][adjacentCol] == 0:
                    flag = True
                    if not output[row][col] == 0:
                        output[row][col] += 1
                queue.append((adjacentRow, adjacentCol))

            print(output)
        print(visited)
        return output

    def getAdjacent(self, mat, row, col, visited):
        adjacents = []
        m = len(mat)
        n = len(mat[0])
        if row + 1 < m and not visited[row + 1][col]:
            adjacents.append((row + 1, col))
        if row - 1 >= 0 and not visited[row - 1][col]:
            adjacents.append((row - 1, col))

        if col + 1 < m and not visited[row][col + 1]:
            adjacents.append((row, col + 1))
        if col - 1 >= 0 and not visited[row][col - 1]:
            adjacents.append((row, col - 1))
        return adjacents


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    sol = Solution()
    print(sol.updateMatrix(mat))
