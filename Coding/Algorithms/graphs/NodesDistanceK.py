from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class NodesDistanceK:

    graph = defaultdict(list)
    # Map<Pair,List<TreeNode>> parent = new HashMap<>();
    # parent.put(new Pair(node.val,,new

    def populateParents(self,root,node=None):
        if root:
            self.graph[root.val].append(node)
            self.populateParents(root.left,root)
            self.populateParents(root.right,root)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        self.populateParents(root,None)
        answer = self.findNodesAtDistanceK(target,k)
        return [] if not answer else answer

    def findNodesAtDistanceK(self,target:TreeNode,k:int)->List[int]:
        queue = deque()
        queue.append([target,0])
        visited = set()
        output = []
        while queue:
            node, distance = queue.popleft()

            if distance==k:
                for curr,curr_distance in queue:
                    output.append(curr.val)
                output.append(node.val)
                return output

            connectedNodes = [node.left,node.right,self.graph[node.val]]
            for node in connectedNodes:
                if not node:
                    continue
                if node in visited:
                    continue
                visited.add(node)
                queue.append([node,distance+1])



        #return output





