"""
LeetCode Problem: https://leetcode.com/problems/find-eventual-safe-states/?envType=study-plan-v2&envId=graph-theory
"""
from collections import defaultdict, deque
from typing import List


class SafeNodes:

    graph = defaultdict(list)
    safe_nodes = []
    WHITE=0
    GRAY=1
    BLACK=2
    states = {'WHITE':0,'GRAY':1,'BLACK':2}
    node_states = defaultdict(int)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        if n==0:
            return self.safe_nodes
        i=0
        for j in range(n):
            self.node_states[j]=self.WHITE
        out_degree = [0 for _ in range(n)]
        in_degree = [0 for _ in range(n)]
        for edge in graph:
            for node in edge:
                self.graph[i].append(node)
                out_degree[i]+=1
                in_degree[node]+=1
            i+=1

        terminal_nodes = [i for i in range(n) if not out_degree[i]]
        self.safe_nodes.extend(terminal_nodes)

        for i in range(n):
            if terminal_nodes[i]:
                continue

            if self.dfs_util(i, terminal_nodes):
                self.safe_nodes.append(i)
        return sorted(self.safe_nodes)

    def dfs_util(self,node,terminal_nodes):
        if self.node_states[node]==self.BLACK:
            return False
        self.node_states[node]=self.GRAY
        connected_nodes = self.graph[node]
        for connection in connected_nodes:
            self.node_states[connection]=self.BLACK
            if self.dfs_util(connection,terminal_nodes):
                return True
        self.node_states[node]=self.WHITE
        return False










