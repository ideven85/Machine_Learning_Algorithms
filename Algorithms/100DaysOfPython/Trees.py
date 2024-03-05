
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def insert(root,val):
    if root is None:
        root = TreeNode(val)
    elif val < root.val:
        root.left = insert(root.left,val)
    elif val > root.val:
        root.right = insert(root.right,val)
    return root
from collections import deque
from typing import Optional, List


def minDepth( root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left = minDepth(root.left)
    right = minDepth(root.right)
    answer = min(left,right)
    return 1+(answer if answer else max(left,right))

def minDepthV2( root: Optional[TreeNode]) -> int:
    if root is None:return 0
    if not root.left:
        return 1 + minDepth(root.right)
    elif not root.right:
        return 1 + minDepth(root.left)
    else:
        return 1+ min(minDepth(root.left),minDepth(root))

def minDepth3(root: Optional[TreeNode]) -> int:
    if root is None:return 0
    depth=1
    queue = deque()
    queue.append([root,depth])

    while len(queue)>0:
        node,depth = queue.popleft()
        if node:
            if not node.left and not node.right:
                return depth
            queue.append([node.left,1+depth])
            queue.append([node.right,1+depth])

    return depth
def levelOrder( root: Optional[TreeNode]) -> List[List[int]]:
    output = []
    if not root:
        return output
    queue = deque()

    queue.append(root)
    queue.append(None)
    temp = []

    while queue:
        node = queue.popleft()
        if node: # Node does not exist when we reach next level
            temp.append(node.val)
            print(temp,end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            output.append(temp)
            temp = []
            print()
            if queue:
                for node in queue:
                    print(node.val,end=' ')

                queue.append(None) # We Append None to signal we have reached next level
                # Logic? Another Solution?
    return output

def maxAncestorDiff( root: Optional[TreeNode]) -> int:
    pass



if __name__ == '__main__':
    root = TreeNode(6)
    insert(root,10)
    insert(root,11)
    insert(root,4)
    insert(root,15)
    insert(root,2)
    insert(root,5)
    print(levelOrder(root))
    print(minDepthV2(root))
    print(minDepth3(root))