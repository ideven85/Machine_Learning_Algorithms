from collections import defaultdict, deque
from typing import List

"""
Questions Passed On Site Assessment
But Score Python: 4.79
Need to improve python
"""

"""
public static boolean canFinish(int numCourses, int[][] prerequisites){
        int V = numCourses-1;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[1]).add(prerequisite[0]);

        }
        int[] in_degree = new int[numCourses];
        for (int u = 0; u < numCourses; u++) {
            for(int adjacent:adj.get(u))
                in_degree[adjacent]++;
        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if(in_degree[i]==0)
                queue.add(i);
        }
        int count = 0;
       // boolean[] visited = new boolean[numCourses];
        while(!queue.isEmpty()){
            int current = queue.poll();

            count++;
            for(var adjacent:adj.get(current)){
                if(--in_degree[adjacent]==0)
                    queue.add(adjacent);
            }


        }
        System.out.println(count);
        return count == numCourses;
    }

    public static void main(String[] args) {
        //numCourses = 2, prerequisites = [[1,0]]
        int numCourses = 2;
        int[][] preRequisites = {{1,0}};
        System.out.println(canFinish(numCourses,preRequisites));
    }
}
"""
class CoursePreRequisites:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = dict(list)
        for req in prerequisites:
            adj[req[1]].get
        in_degree = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            for u in adj[i]:
                in_degree[u]+=1
        queue = deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        count = 0
        while queue:
            current = queue.popleft()
            count+=1
            for adjacent in adj[current]:
                in_degree[adjacent]-=1
                if in_degree[adjacent]==0:
                    queue.append(adjacent)
        return count==numCourses

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses==1:
            return [0]
        adj = defaultdict(list)
        for req in prerequisites:
            adj[req[1]].append(req[0])
        in_degree = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            for adjacent in adj[i]:
                in_degree[adjacent]+=1
        queue = deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        courseOrdering = [0 for _ in range(numCourses)]
        count = 0
        while queue:
            current = queue.pop()
            courseOrdering[count]=current
            count+=1
            for adjacent in adj[current]:
                in_degree[adjacent]-=1
                if in_degree[adjacent]==0:
                    queue.append(adjacent)

        return courseOrdering if count==numCourses else []
