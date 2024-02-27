from collections import defaultdict, deque
from typing import List


class TownJudge(object):

    #todo
    def findJudgeIncorrect(self, n: int, trust: List[List[int]]) -> int:

        t = [False for _ in range(n+1)]
        in_degree = [0 for _ in range(n+1)]
        mapping = defaultdict(list)
        for a, b in trust:
            mapping[a].append(b)
            in_degree[b] += 1

        """
        BFS Traversal
        """
        visited = [False for _ in range(n+1)]
        visited[0] = True
        queue = deque()
        in_degree[0]=1
        for i in range(1,n+1):
            if in_degree[i]==0:
                queue.append(i)

        while queue:
            current_node = queue.popleft()





        for i in range(1,n+1):
            if not t[i]:
                return i

        return -1


    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        in_degree = [0 for _ in range(n+1)]
        out_degree = [0 for _ in range(n+1)]
        for a, b in trust:
            #graph[a].append(b)
            in_degree[b]+=1
            out_degree[a]+=1


        for i in range(1,n+1):
            if in_degree[i]==n-1 and out_degree[i]==0:
                return i
        return -1

n = 2; trust = [[1,2]]
n1 = 3; trust1 = [[1,2],[2,3]]
print(TownJudge().findJudge(n,trust))
print(TownJudge().findJudge(n1,trust1))
