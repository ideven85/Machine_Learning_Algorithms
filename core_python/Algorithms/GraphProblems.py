from collections import deque
from functools import lru_cache
from typing import List


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array=array)
        return array

    def breadthFirstSearch(self, array):
        # Write your code here.
        pass


class Graph:
    adj = []

    def addEdge(self, u, v, isDirected):
        self.adj[u].append(v)
        if not isDirected:
            self.adj[v].append(u)

    def dfsUtil(self, source, destination, count):
        if source == destination:
            return count
        else:

            for u in self.adj[source]:
                count += 1
                self.dfsUtil(u, destination=destination, count=count)
        return count

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        W = len(edges)

        a = [1]
        for _ in range(n):
            self.adj.append([])
        count = 0
        for i in range(n):
            self.addEdge(edges[i][0], edges[i][1], True)
        count = self.dfsUtil(source, destination, count)
        return count == 0


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:

    target = len(graph) - 1
    results = []

    def backtrack(currNode, path):
        # if we reach the target, no need to explore further.
        if currNode == target:
            results.append(list(path))
            return
        # explore the neighbor nodes one after another.
        for nextNode in graph[currNode]:
            path.append(nextNode)
            backtrack(nextNode, path)
            path.pop()

    # kick of the backtracking, starting from the source node (0).
    path = deque([0])
    backtrack(0, path)

    return results


"""
    For DP Solution
    nextNode∈neighbors(currNode),allPathsToTarget(currNode)={currNode+allPathsToTarget(nextNode)}
"""


def allPathsSourceTargetV2(graph: List[List[int]]) -> List[List[int]]:

    target = len(graph) - 1

    # apply the memoization
    @lru_cache(maxsize=None)
    def allPathsToTarget(currNode):
        if currNode == target:
            return [[target]]

        results = []
        for nextNode in graph[currNode]:
            for path in allPathsToTarget(nextNode):
                results.append([currNode] + path)

        return results

    return allPathsToTarget(0)


def dfsUtil(array, source, visited):
    visited[source] = True
    i = 0
    target = 0
    while i != source:
        print(visited)
        target += array[i]
        visited[i] = True
        i += 1

    print()

    return False


def hasSingleCycle(array):
    jumps = 0
    position = 0

    while True:
        position += array[position]
        position %= len(array)
        print(position, end=" ")
        jumps += 1

        if position == 0 or array[position] == 0 or jumps > len(array):
            break
    print()
    return jumps == len(array)


def hasSingleCycleV2(array):
    # Write your code here.
    visited = [False for _ in range(len(array))]
    n = len(array)
    for i in range(n):
        visited = [False for _ in range(len(array))]
        if not dfsUtil(array, i, visited):
            return False
    return True


def hasSingleCycleV4(array):
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


def hasSingleCycleV5(array):
    correct_cycles = 0
    jumps = 0
    n = len(array)
    for i in range(n):
        vertex = i
        jumps = 0
        for j in range(n):
            jumps += array[j]
            jumps = jumps % n
            if jumps == i:
                print(jumps)
                correct_cycles += 1
                break

    print(correct_cycles)
    return correct_cycles == n - 1


def maximumScore(nums: List[int], multipliers: List[int]) -> int:
    pointer1 = 0
    n = len(nums)
    pointer2 = len(nums) - 1
    m = len(multipliers)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for left in range(i, -1, -1):
            mult = multipliers[i]
            right = n - 1 - (i - left)
            dp[i][left] = max(
                mult * nums[left] + dp[i + 1][left + 1],
                mult * nums[right] + dp[i + 1][left],
            )
        print(dp)
    return dp[0][0]


#!/bin/python3

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#


def maximumSum(a, m):
    max_so_far = 0
    total = 0
    current = 0
    left = 0
    for i in range(len(a)):

        if a[i] % m == m - 1:
            return m - 1
        if max_so_far == m - 1:
            return max_so_far
        max_so_far += a[i]

        if total <= max_so_far:
            total = max_so_far
        if total % m == m - 1:
            print("Foo", total)
            return m - 1
        if max_so_far > m:
            left = i
            while max_so_far > m and left >= 0:
                max_so_far -= a[left]
                left -= 1
        print(left)

        i = left
        print("Max", max_so_far, end=" ")
    print(total)
    return total % m


def maximumScoreV2(nums: List[int], multipliers: List[int]) -> int:
    # lru_cache from functools automatically memoizes the function
    @lru_cache(2000)
    def dp(i, left):
        # Base case
        if i == m:
            return 0

        mult = multipliers[i]
        right = n - 1 - (i - left)

        # Recurrence relation
        return max(
            mult * nums[left] + dp(i + 1, left + 1),
            mult * nums[right] + dp(i + 1, left),
        )

    n, m = len(nums), len(multipliers)
    return dp(0, 0)


if __name__ == "__main__":
    a = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycleV5(a))

    nums1 = [1, 2, 3]
    multipliers = [3, 2, 1]
    print(maximumScore(nums1, multipliers))
    a = [1, 5, 3, 22, 30, 2, 5]
    print(maximumSum(a, 2))
