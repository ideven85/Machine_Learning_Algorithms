from collections import defaultdict
from typing import List


class Safe_Nodes:



    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:


        adj = defaultdict(list)
        white = 0
        gray = 1
        black = 2

        def safeNodeHelper(node):

            if visited[node] and node not in terminalNodes:
                return False
            visited[node] = True
            for connection in adj[node]:

                if visited[connection] and connection not in terminalNodes:
                    return False

                if safeNodeHelper(connection):
                    return True
            visited[node]=False
            print(visited)

            return True


        terminalNodes = []
        out = []

        if not graph:
            return out
        n = len(graph)
        i=0
        visited = [False for _ in range(n)]
        for nodes in graph:
            if not nodes:
                terminalNodes.append(i)
                visited[i]=True
            adj[i].extend([node for node in nodes])
            i+=1

        for i in range(n):
            if i in terminalNodes:
                out.append(i)
            else:
                if safeNodeHelper(i):
                    out.append(i)
        print(visited)
        return sorted(out)


s = Safe_Nodes()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(s.eventualSafeNodes(graph))