from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinaryTree:
    
    def insert(self,root:Optional[TreeNode],value:int):
        if not root:
            root = TreeNode(value)
        elif value<root.val:
            root.left=self.insert(root.left,value)
        elif value>root.val:
            root.right = self.insert(root.right,value)
        return root

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.val,end=' ')
            self.inOrder(root.right)
        
    def maxDepth(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root,1))
        result = 0
        while len(queue):
            current,depth = queue.popleft()
            result = max(result,depth)
            if current.left:
                queue.append((current.left,depth+1))
            if current.right:
                queue.append((current.right,depth+1))
        return result

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,value):
            if not node:
                return 0
            if not node.left and not node.right:
                return value+node.val==targetSum
            value+=node.val
            left = dfs(node.left,value)
            right = dfs(node.right,value)
            return left or right




        return dfs(root,0)

    ans = 1234000

    def minDepth(self, root: Optional[TreeNode]) -> int:


        def dfs(current,depth):
            if not current:
                return 0
            if not current.left and not current.right:
                self.ans = min(depth,self.ans)
            left = dfs(current.left,depth+1)
            right = dfs(current.right,depth+1)
            return min(left,right)


        dfs(root,1)
        return self.ans if root else 0



if __name__ == '__main__':
    tree = BinaryTree()
    root = TreeNode(10)
    tree.insert(root,5)
    tree.insert(root,15)
    tree.insert(root,20)
    tree.insert(root,22)
    tree.insert(root,6)
    tree.insert(root,4)
    tree.insert(root,8)
    tree.insert(root,2)
    tree.insert(root,12)
    tree.insert(root,17)
    tree.insert(root,11)
    tree.inOrder(root)
    print(tree.maxDepth(root))
    print(tree.hasPathSum(root,67))
    print(tree.minDepth(root))


