from collections import defaultdict, deque
from typing import List

class Solution:
    def findCircleNum(self, cnx: List[List[int]]) -> int:
        res=0
        n=len(cnx)
        def dfs(i):
            cnx[i][i]=2
            for j in range(0,n):
                if cnx[i][j]==1:
                    cnx[i][j]=2
                    dfs(j)
        for i in range(0,n):
            if cnx[i][i]==1:
                res+=1
                dfs(i)
        return res
class NumberOfProvinces:


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
            isConnected = [[1,1,0],[1,1,0],[0,0,1]]
            Given a list of cities starting at 1, we need to find the number
                of cities which are directly or indirectly connected

            Problem can be solved easily using Union Find...
             Let us try an alternate approach

        """
        cityMap = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                cityMap[i+1].append(isConnected[i][j])
        n = len(isConnected)
        visited = [False for _ in range(n+1)]
        visited[0]=True
        count = [0]
        queue = deque()
        queue.append(1)
        for city in range(1,n+1):

            print(self.dfsUtil(cityMap,city,visited,count),end=' ')

        print('\n',visited)
        print("Count: ",count[0])
        count=0
        for e in visited:
            if not e:
                count+=1
        print(count)
        return n-count+1



    def dfsUtil(self,cityMap,current,visited,count):




        connections = cityMap[current]
        for connection in connections:
            if visited[connection]:
                continue
            if current==connection:
                continue
            visited[connection]=True
            count[0] += 1
            #print(count)
            self.dfsUtil(cityMap,connection,visited,count)

        return count


class NumberOfProvincesUF:


    def init(self,n):
            self.root = [0 for _ in range(n+1)]
            self.count = n

    def find(self,city):
        if city!=self.root[city]:
            self.root[city]=self.find(self.root[city])
        return self.root[city]




    def union(self,city1,city2):
            root1 = self.find(city1)
            root2 = self.find(city2)
            if root1!=root2:
                print('hi',end=' ')
                self.root[root2]=root1
                self.count-=1



    graph = defaultdict(list)
    def findCircleNum(self, cnx: List[List[int]]) -> int:
        # n = len(cnx)
        # if n<=1:
        #     return n
        # for i in range(n):
        #     for city in cnx[i]:
        #         if city==1 and i!=city:
        #             self.graph[i].append(city)
        # visited = [False for _ in range(n+1)]
        # visited[0]=True
        # connections = [0]
        # for city in range(n):
        #     if visited[city]:
        #         continue
        #     self.dfs(city,visited,connections)
        # print(connections)
        # return n-connections[0]-1
        print(cnx)
        self.init(len(cnx))
        for i in range(len(cnx)):
            for j in range(len(cnx[i])):
                if cnx[i][j]==1:
                    self.union(i,j)
        print(self.root)
        return self.count

    def dfs(self,current,visited,count):

        connections = self.graph[current]
        for connection in connections:
            if visited[connection]:
                continue
            visited[connection]=True
            return self.dfs(connection,visited,count[0]+1)
        return count[0]


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    isConnected1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    #print(NumberOfProvinces().findCircleNum(isConnected))
    #print(NumberOfProvinces().findCircleNum(isConnected1))
    sol = Solution()
    #print(sol.findCircleNum(isConnected))
    #print(sol.findCircleNum(isConnected1))
    print("Number of Provinces: ",NumberOfProvincesUF().findCircleNum(isConnected))