from collections import defaultdict, deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        rooms = [[1],[2],[3],[]] return True
        """
        roomMap = defaultdict(list)
        n = len(rooms)
        for i in range(n):
            for j in range(len(rooms[i])):
                roomMap[i].append(rooms[i][j])
        count = 0
        queue = deque()
        visited = [False for _ in range(n)]
        queue.append(0)
        while len(queue):
            current = queue.popleft()
            if visited[current]:
                continue
            visited[current] = True
            count += 1
            if count >= n:
                return True
            keys = roomMap[current]
            if len(keys) > 0:
                for e in keys:
                    queue.append(e)
        return count >= n


if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    rooms1 = [[1, 3], [3, 0, 1], [2], [0]]
    print(Solution().canVisitAllRooms(rooms))
    print(Solution().canVisitAllRooms(rooms1))
