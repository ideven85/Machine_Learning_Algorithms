from collections import deque
from typing import List


"""
BFS
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        pass


"""
DFS
"""


def hasSingleCycle(array):
    n = len(array)
    jumps = 0
    current_position = 0
    while True:
        current_position += array[current_position]
        current_position = current_position % n
        jumps += 1
        if current_position == 0 or array[current_position] == 0 or jumps > len(array):
            break

    return jumps == n


def riverSizes(matrix):
    # Write your code here.
    output = []
    n = len(matrix)
    visited = [[False for value in row] for row in matrix]
    for row in range(n):
        for col in range(len(matrix[row])):
            if visited[row][col]:
                continue
            size = dfsUtil(matrix, row, col, visited)
            if size > 0:
                output.append(size)
    return output


def adjacent(matrix, row, col, visited):
    positions = []
    n = len(matrix)
    m = len(matrix[row])
    if row - 1 > 0 and not visited[row - 1][col]:
        positions.append([row - 1, col])
    if row < n - 1 and not visited[row + 1][col]:
        positions.append([row + 1, col])
    if col - 1 > 0 and not visited[row][col - 1]:
        positions.append([row, col - 1])

    if col < m - 1 and not visited[row][col + 1]:
        positions.append([row, col + 1])

    return positions


def dfsUtil(matrix, row, col, visited):
    count = 0
    nodesToExplore = deque()
    nodesToExplore.append([row, col])
    while len(nodesToExplore) > 0:
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue

        if matrix[i][j] == 0:
            continue
        visited[i][j] = True
        count += 1
        unvisited = adjacent(matrix, i, j, visited)
        # print(unvisited)
        if len(unvisited) > 0:
            for neighbour in unvisited:
                nodesToExplore.append(neighbour)
    # print(visited)
    return count


class DjiskstraAlgorithm:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = dict()
        for e in times:
            if e[0] not in adj:
                current = [[e[1], e[2]]]
                adj[e[0]] = current
            else:
                current = adj.get(e[0])
                current.append([e[1], e[2]])
                adj[e[0]] = current
        print(adj)
        adj = dict(sorted(adj.items(), key=lambda item: item[1], reverse=True))
        print(adj)

        visited = set()
        totalTime = 0
        # print(adj)
        signalReceivedAt = [float("inf") for _ in range(n + 1)]

        self.depthFirstSearch(adj, k, visited, signalReceivedAt, totalTime)
        answer = -float("inf")
        for i in range(1, n + 1):
            answer = max(answer, signalReceivedAt[i])
        # print(signalReceivedAt)
        # print("\n TotalTime:",totalTime)
        """ if destination in visited:
                continue

            visited.add(destination)
            #totalTime+=weight
            if len(visited)==n:
                break

            
            connectedNodes = adj.get(destination)
            print(connectedNodes)
            if connectedNodes:
                for adjacent,adjacentWeight in connectedNodes:
                    if adjacent in visited:
                        continue
                    temp = []
                    temp.append(adjacentWeight)
                    
                    
                    
                    queue.append(adjacent)
        """
        return -1 if answer == float("inf") else answer

    def depthFirstSearch(self, adj, source, visited, signalReceivedAt, totalTime):

        if totalTime >= signalReceivedAt[source]:
            return

        # visited.add(source)
        # print(totalTime,end=' ')
        connectedNodes = adj.get(source)
        signalReceivedAt[source] = totalTime

        if connectedNodes:

            for adjacent, weight in connectedNodes:
                if adjacent:
                    if adjacent in visited:
                        continue

                    self.depthFirstSearch(
                        adj,
                        adjacent,
                        visited=visited,
                        signalReceivedAt=signalReceivedAt,
                        totalTime=totalTime + weight,
                    )


if __name__ == "__main__":
    m = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(riverSizes(m))
    a = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycle(a))
    dj = DjiskstraAlgorithm()
    times = [[2, 1, 2], [2, 3, 3], [3, 4, 1], [3, 1, 2], [1, 2, 3]]
    n = 4
    k = 2
    t1 = [[1, 2, 1]]
    n1 = 2
    k1 = 1
    print(dj.networkDelayTime(times, n, k))
    print(dj.networkDelayTime(t1, n1, k1))
