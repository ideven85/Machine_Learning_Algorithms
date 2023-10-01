# This is an input class. Do not edit.
from collections import deque
from queue import Queue
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        if not root:
            root = BST(value=value)
        elif value==root.value:
            root = BST(value=value)
        elif value<root.value:
            root.left = self.insert(value)
        elif value>root.value:
            root.right = self.insert(value)
        return self



    def contains(self, value):
        # Write your code here.
        root = self
        if not root:
            return False
        queue = deque()
        queue.append(root)

        while queue is not None:
            current = queue.popleft()
            if current == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    result = []
    """def inOrder(self):
        if self.root is not None:
            self.root.left = self.inOrder()
            self.result.append(self.root.value)
            self.root.right = self.inOrder()
        return self.root
    """

    def levelOrderTraversal(self):
        """
        Level Order Traversal of Binary Tree
        :return: List of Nodes
        """
        root = self
        if root is None:
            return
        queue = deque()

        queue.append(root)
        queue.append(None)

        while len(queue) >= 1:
            current = queue.popleft()
            if current:
                self.result.append(current.value)
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        root = self
        self.levelOrderTraversal()
        if value in self.result:
            self.result.remove(value)
            root = None
            for e in self.result:
                self.insert(e)

        return self



class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, root, val):
        if root is None:
            root = TreeNode(val=val)
        elif val < root.val:
            root.left = self.insert(root.left, val=val)
        elif val > root.val:
            root.right = self.insert(root.right, val=val)
        return root

    def inOrder(self, root, answer):
        if root is not None:
            self.inOrder(root.left, answer=answer)
            answer.append(root.val)
            self.inOrder(root.right, answer=answer)
        return answer

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        return self.inOrder(root, answer=answer)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = self.inorderTraversal(root)
        return answer[k]

    def kthSmallestV2(self, root: Optional[TreeNode], k: int) -> int:

        pointer = 0
        queue = deque()
        current = root
        while len(queue) > 0 or current is not None:
            # print(pointer,end=' ')

            if current:

                queue.append(current)
                current = current.left


            else:

                current = queue.pop()
                pointer = pointer + 1
                if pointer == k:
                    return current.val
                # print(current.val,end=' ')

                current = current.right

    def closestValue(self, root, target):
        if not root:
            return 0
        if target <= root.val:
            return root.val
        if root.left is None and root.right is None:
            return root.val
        # print(root.val,end=' ')
        if root.left and target >= root.left.val:
            if root.val - target > target - root.left.val:
                return root.left.val
            else:
                return root.val

        if root.right and target <= root.right.val:
            if target - root.val > root.right.val - target:
                return root.right.val
            else:
                return root.val
        if root.left:
            self.closestValue(root.left, target)
        if root.right:
            self.closestValue(root.right, target)
        else:
            return -1





def inOrder(root):
    if root is not None:

        inOrder(root.left)
        print(root.val,end=' ')
        inOrder(root.right)

class TreeInfo:
    def __init__(self,diameter, height):
        self.diameter = diameter
        self.height = height

def insert(root,value):
    if root is None:
        root = TreeNode(value)
    elif value==root.val:
        root.right = TreeNode(value)
    elif value<root.val:
        root.left=insert(root.left,value)
    elif value>root.val:
        root.right = insert(root.right,value)
    return root


def levelOrderTraversal(root):
    """
    Level Order Traversal of Binary Tree
    :param root: Root of the tree
    :return: None
    """
    if root is None:
        return
    queue = deque()

    queue.append(root)
    queue.append(None)

    while len(queue)>=1:
        current = queue.popleft()
        if current:

            if current.left:
                queue.append(current.left)


            if current.right:
                queue.append(current.right)

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

def heightBalancedBinaryTreeV2(root):
    balanced = [True]
    balancedHeightUtil(root,balanced)
    return balanced[0]

def balancedHeightUtil(root, balanced):
    if root is None:
        return 0
    left = balancedHeightUtil(root.left,balanced)
    right = balancedHeightUtil(root.right,balanced)
    if (left+right)>1:
        balanced[0]=False
    treeHeight = 1+max(left,right)
    return treeHeight


def maxPathSum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    current_sum = 0;max_sum=0
    queue = deque()
    queue.append(root)
    while queue:
        current_node=queue.popleft()
        current_sum+=current_node.val
        if max_sum<=current_sum:
            max_sum=current_sum
def sumNumbers(root: Optional[TreeNode]) -> int:
    path_sum=0
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    queue.append(None)
    curr = []
    paths = []
    path_sum=root.val
    level = 1
    while queue:

        current = queue.popleft()
        if current:
            curr.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            level*=10
        else:
            current_sums = []
            for e in curr:
                current_sums.append(path_sum+level*e)
            if not queue:
                queue.append(None)

            curr=[]
            paths.append(current_sums)
        for e in paths[-1]:
            s = list(e)
            s.reverse()
            for f in s:
                path_sum+=f
        return path_sum


def calcSum(root,current,sum):
    if not root:
        return
    current = current*10+root.val
    if not root.left and not root.right:
        sum[0]+=current
        print(sum[0])
    calcSum(root.left,current,sum)
    calcSum(root.right,current,sum)

def sumNumbersV2(root):
    if root is None:
        return 0
    current = 0
    sum = [0]
    calcSum(root,current,sum)
    return sum[0]

def sumNumbersV3( root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        globalsum = [0]

        def dfs(node, sum):
            sum = sum * 10 + node.val

            if node.left is None and node.right is None:
                globalsum[0] += sum


            if node.left:
                dfs(node.left, sum)

            if node.right:
                dfs(node.right, sum)

        dfs(root, 0)
        return globalsum[0]









def depth(root,value):
    if root is None:
        return 0
    if root.value == value:
        return 0
    if value<root.value:
        return 1+depth(root.left,value)
    elif value>root.value:
        return 1+depth(root.right,value)
    return 0

def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter

def getTreeInfo(root):
    if root is None:
        return TreeInfo(0,0)

    left = getTreeInfo(root.left)
    right = getTreeInfo(root.right)
    longestPathThroughRoot = left.height+right.height
    maxDiameterSoFar = max(left.diameter,right.diameter)
    currentDiameter = max(longestPathThroughRoot,maxDiameterSoFar)
    currentHeight = 1+max(left.height,right.height)

    return TreeInfo(currentDiameter,currentHeight)

def invertBinaryTree(root):
    # Write your code here.
    if root is None:
        return None
    if root.left and root.right:
        temp = root.left
        root.left=root.right
        root.right=temp
    elif root.left is not None:
        root.left = root.right
    elif root.right is not None:
        root.right = root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    return root



class InorderSuccessor:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.parent = None

    def inorderSuccessor(self, node: Node) -> Optional[Node]:
        if not node:
            return None
        if node.right:
            return self.leftMostChild(node.right)
        else:
            q = node
            x = node.parent
            while x and x.left!=q:
                q=x
                x=x.parent
            return x



    def leftMostChild(self,node):
        if not node:
            return None
        while node.left:
            node=node.left
        return node


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    pass
def invertBinaryTreeV2(root):
    if root is not None:
        invertBinaryTree(root.left)
        invertBinaryTree(root.right)
        temp = root.left
        root.left=root.right
        root.right=temp
    return root


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    root = None;flag = False
    if nodeOne.value>=nodeTwo.value:
        root = nodeOne
        flag = True
    elif nodeThree.value>=nodeTwo.value:
        root = nodeThree

    if  flag:
        node = lca(root,nodeTwo,nodeThree)
        if node:
            if node.value == root.value:
                return True

    else:
        node = lca(root,nodeTwo,nodeOne)
        if node:
            if node.value == root.value:
                return True

    return False

def lca(root,node1,node2):
    if root is None:
        return None

    elif root.val == node1 or root.val == node2:
        return root
    lca1 = lca(root.left,node1,node2)
    lca2 = lca(root.right,node1,node2)
    if lca1  and lca2:
        return root
    elif lca1:
        return lca1
    else:
        return lca2

def mergeBinaryTrees(tree1:BinaryTree, tree2:BinaryTree):
    # Write your code here.
    if not tree1 and not tree2:
        return None
    elif not tree1:
        return tree2
    elif not tree2:
        return tree1
    tree1.value+=tree2.value
    tree1.left = mergeBinaryTrees(tree1.left,tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right,tree2.right)

def flattenBinaryTree(root:TreeNode)->TreeNode:
    # Write your code here.
    if not root:
        return None
    answer = {}
    queue = deque()
    queue.append([0,root])
    while len(queue)>0:
        height,current = queue.popleft()
        if not answer:
            answer[height]=[current]

        else:
            if answer.get(height) is not None:
                answer[height]=answer[height]+[current]
            else:
                answer[height]=[current]


        if current.left:
            queue.append([height-1,current.left])
        if current.right:
            queue.append([height+1,current.right])
    node = None;temp=None
    root = node
    current_height=0
    #print(answer)
    while answer is not None:
        if answer.get(current_height) is None:
            break
        curr = answer[current_height]

        for rightNode in curr:
            if not node:
                node = rightNode
                temp = node
                root=node
                current_height+=1
            else:
                node.right = rightNode
                node.left = temp
                temp=node
                node=node.right
                current_height+=1
    return root


def zigzagLevelOrder( root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    currentLevel = []
    leftToRight = True
    if root:
        currentLevel.append(root)
    while len(currentLevel)>0:
        levelResult = []
        nextLevel = []
        while len(currentLevel)>0:
            node = currentLevel.pop()
            levelResult.append(node.val)
            if leftToRight:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            else:
                if node.right:
                    nextLevel.append(node.right)
                if node.left:
                    nextLevel.append(node.left)
        currentLevel=nextLevel

        result.append(levelResult)
        #print(result,end=' ')
        leftToRight=not leftToRight
    return result












def rightSiblingTree(root):
    # Write your code here.
    pass




if __name__ == '__main__':
    bt = TreeNode(5)
    insert(bt,3)
    insert(bt,6)
    insert(bt,7)
    insert(bt,8)
    inOrder(bt)
    print()

    print(zigzagLevelOrder(bt))






