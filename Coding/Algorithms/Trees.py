from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def insert(self,root,val):
        if not root:
            root = TreeNode(val)
        elif val<root.val:
            root.left=self.insert(root.left,val)
        elif val>root.val:
            root.right=self.insert(root.right,val)
        return root
    output = []
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            self.output.append(root.val)
            print(root.val,end=' ')
            self.inOrder(root.right)

    def findPaths(self,root:Optional[TreeNode],path,paths):
        if root is None:
            return paths
        if root.left is None and root.right is None:
            temp=str()
            for i in range(len(path)-1):
                temp+=path[i]+"->"
            temp+=path[len(path)-1]
            paths.append(temp)
            #paths.append(path)

        self.findPaths(root.left,path+[str(root.val)],paths)
        self.findPaths(root.right,path+[str(root.val)],paths)
        return paths

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if root is None:
            return paths
        path=[]
        return self.findPaths(root,path,paths)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Vertical Order Traversal
        Problem Variants Top View, Right Side View
        """
        output = []
        levels  = {}
        if root is None:
            return output
        queue = deque()
        queue.append(self.Pair(root,0))
        while queue:
            current = queue.popleft()
            curr_node = current.node
            curr_height = current.height
            if curr_height-1 not in levels:
                levels[curr_height-1]=curr_node
            if curr_node.right:
                queue.append(self.Pair(curr_node.right,curr_height+1))
            if curr_node.left:
                queue.append(self.Pair(curr_node.left, curr_height - 1))

        for k,v in levels.items():
            output.append(v.val)

        return output
    def rightSideViewV2(self,root):
        if not root:
            return []
        queue,res = [root],[]
        while queue:
            diameter = len(queue)
            for i in range(diameter):
                current = queue.pop(0)
                if i==diameter-1: res.append(current.val)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
        return res

    def rightSideViewV3(self, root: Optional[TreeNode]) -> List[int]:
        """

        :param root:
        :return:
        """
        q = deque()
        if root: q.append(root)
        ans = []

        while q:
            node = None
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if node: ans.append(node.val)

        return ans

    class Pair:
        def __init__(self,node:Optional[TreeNode]=None,height=0):
            self.node=node
            self.height = height


    def topView(self,root: Optional[TreeNode]):
        if root is None:
            return []
        output = {}
        queue = deque()
        queue.append(self.Pair(root,0))
        while queue:
            current = queue.popleft()
            node = current.node
            height = current.height
            if height not in output:
                output[height]=node
            if node.left:
                queue.append(self.Pair(node.left,height-1))
            if node.right:
                queue.append(self.Pair(node.right,height+1))
        for k,v in output.items():
            print(v.val,end=' ')



    def populateParents(self,root, node,parents):
        if root:
            parents[root.val] = node
            self.populateParents(root.left, root,parents)
            self.populateParents(root.right, root,parents)





    def findNodesDistanceK(self,root, target, k):
        # Write your code here.
        parents = {}
        self.populateParents(root,None,parents)
        #print(parents[root.val])
        #targetNode=self.getNodeFromValue(root,parents,target)


        output = self.bfs(target,parents,k)
        
        return [] if output is None else output

    def bfs(self,startingNode:TreeNode,parents:dict,k:int)->List[int]:
        queue = deque()
        queue.append([0,startingNode])
        seen = {startingNode}
        output= []
        while len(queue)>0:
            [currentDistance,currentNode] = queue.popleft()

            if currentDistance == k:
                for (k,v) in queue:
                    output.append(v.val)
                #output.append(node)
                output.append(currentNode.val)
                return output

            connectedNodes = [currentNode.left,currentNode.right,parents[currentNode.val]]
            for node in connectedNodes:
                if node is None:
                    continue
                if node in seen:
                    continue
                seen.add(node)
                queue.append([currentDistance+1,node])





    """def findNodesAtDistanceK(self,root,target,k):
    
        Given the root of the binary tree
        And a Target Node
        Find All Nodes which are at distance k from the target node
        
        parents = {}
        self.findParentNodes(root,None,parents,target)
        targetNode = self.getNodeFromValue(root,parents,target)
        return self.bfsOfNodesAtDistanceKFromTarget(targetNode,parents,k)
"""
    def findParentNodes(self,root,temp,parents,target):
        if root is None:
            return

        parents[root.val]=temp
        self.findParentNodes(root.left,root,parents,target)
        self.findParentNodes(root.right,root,parents,target)

    def getNodeFromValue(self,root,parents,target):
        if root.val == target:
            return root
        parentNode = parents[target]
        if parentNode.left and parentNode.left.val == target:
            return parentNode.left
        return parentNode.right

    # def bfsOfNodesAtDistanceKFromTarget(self,targetNode,parents,k):
    #     output = []
    #     seen = set()
    #     seen.add(targetNode)
    #     distance = 0
    #     queue = deque()
    #     queue.append([0,targetNode])
    #     while queue:
    #         [current_distance,current_node]=queue.popleft()
    #         if current_node:
    #             if current_distance ==k:
    #                 output.append(current_node.val)
    #             if current_distance > k:
    #                 break
    #             seen.add(current_node)
    #             node = parents[current_node.val]
    #             if node not in seen:
    #                 queue.append([distance+1,node])
    #     return output



    def lca(self,root,k,v):
        if root is None:
            return
        if root.val == k or root.val == v:
            return root
        lca1 = self.lca(root.left,k,v)
        lca2 = self.lca(root.right,k,v)
        if lca2 and lca1:
            return root
        elif lca1:
            return lca1
        else:
            return lca2

    def validateThreeNodesV2(self,nodeOne, nodeTwo, nodeThree):
        return (self.isChild(nodeOne,nodeTwo) and self.isChild(nodeTwo,nodeThree)) or (self.isChild(nodeThree,nodeTwo) and self.isChild(nodeTwo,nodeOne))

    def isChild(self,root,child):
        while root is not None and root is not child:
            root=root.left if child.val < root.val else root.right
        return root is child

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# def connect(self, root: Optional[Node]) -> Optional[Node]:
#     if not root:
#         return None
#     queue=deque()
#     queue.append([root,0])
#     queue.append(None)
#
#     while len(queue):
#         current = queue.popleft()
#         if current:
#             node,depth = current




def symmetricalTree(tree)->bool:
    # Write your code here.
    if tree is None:
        return True
    queue = [(tree.left,tree.right)]
    while queue:
        left,right = queue.pop(0)
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.value!=right.value:
            return False
        queue.append([left.left,right.right])
        queue.append([left.right,right.left])
    return True



# This is the class of the input root. Do not edit it.






if __name__ == '__main__':
    root = TreeNode(3)
    #node1 = TreeNode(3)
    #node2 = TreeNode(-9)
    bt = BinaryTree(10)
    bt.insert(root,2)
    bt.insert(root, 3)
    bt.insert(root, 4)
    bt.insert(root, 5)
    bt.insert(root,10)
    bt.insert(root,20)
    bt.insert(root,15)
    bt.insert(root,13)
    bt.insert(root,16)

    print("Inorder",bt.inOrder(root))
    bt.inOrder(root)

    print(bt.findNodesDistanceK(root,10,3))
