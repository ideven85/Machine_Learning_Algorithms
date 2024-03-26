"""
LeetCode Problem: https://leetcode.com/problems/find-eventual-safe-states/?envType=study-plan-v2&envId=graph-theory
"""

from collections import defaultdict, deque
from typing import List


class SafeNodes:

    graph = None
    safe_nodes = None
    WHITE = 0
    GRAY = 1
    BLACK = 2
    states = {"WHITE": 0, "GRAY": 1, "BLACK": 2}
    node_states = None

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        if n == 0:
            return self.safe_nodes
        self.node_states = defaultdict(int)
        self.graph = defaultdict(list)
        self.safe_nodes = []
        i = 0
        for j in range(n):
            self.node_states[j] = self.WHITE
            self.graph[j] = list()
        # out_degree = [0 for _ in range(n)]
        # in_degree = [0 for _ in range(n)]
        for edge in graph:
            for node in edge:
                self.graph[i].append(node)
                # out_degree[i]+=1
                # in_degree[node]+=1
            i += 1

        # terminal_nodes = [i for i in range(n) if not out_degree[i]]
        # self.safe_nodes.extend(terminal_nodes)

        for i in range(n):

            if self.dfs_util(i):
                self.safe_nodes.append(i)
        return sorted(self.safe_nodes)

    def dfs_util(self, node):
        if self.node_states[node] == self.GRAY:
            return False
        if self.node_states[node] == self.BLACK:
            return True
        self.node_states[node] = self.GRAY
        connected_nodes = self.graph[node]
        for connection in connected_nodes:
            if self.node_states[connection] == self.WHITE:
                path_exists = self.dfs_util(connection)
                if not path_exists:
                    return False
            elif self.node_states[connection] == self.GRAY:
                return False

        self.node_states[node] = self.BLACK
        return True


if __name__ == "__main__":
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    graph1 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    safe_states = SafeNodes()
    safe_states1 = SafeNodes()
    print(safe_states.eventualSafeNodes(graph))
    print(safe_states1.eventualSafeNodes(graph1))
