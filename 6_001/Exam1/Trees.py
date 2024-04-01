from collections import deque
from dataclasses import dataclass
from typing import Optional



class TreeNode:


    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


def insert(val: int, root: TreeNode) -> TreeNode:
    if not root:
        root = TreeNode(val)
    elif val < root.val:
        root.left = insert(val, root.left)
    elif val > root.val:
        root.right = insert(val, root.right)
    return root


def num_nodes(root: TreeNode) -> int:
    if not root:
        return 0
    left = num_nodes(root.left)
    right = num_nodes(root.right)
    return 1 + left + right


def inOrder(root: TreeNode) -> None:
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)


def numLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return numLeaves(root.left) + numLeaves(root.right)


def printAtDepthK(root: TreeNode, k: int) -> None:
    if not root:
        return
    if k == 0:
        print(root.val, end=" ")
    printAtDepthK(root.left, k - 1)
    printAtDepthK(root.right, k - 1)


def largestValue(root: TreeNode) -> int:
    if not root:
        return 0
    largestLeft = largestValue(root.left)
    largestRight = largestValue(root.right)
    return max(root.val, max(largestLeft, largestRight))


# todo
def maxPathSum(root: Optional[TreeNode]) -> int:
    """
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
    A node can only appear in the sequence at most once.
    Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
    Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    """

    # def dfs(node, is_left=True, left_path=None, right_path=None):
    #     if not node:
    #         return 0
    #     if is_left:
    #         if not node.left:
    #             left_path[node.id]=0
    #             return 0
    #         left_path[node.id] = node.val + max(
    #             dfs(node.left, True, left_path, right_path),
    #             dfs(node.left, False, left_path, right_path),
    #         )
    #
    #         return left_path[node.id]
    #     else:
    #         if not node.right:
    #             right_path[node.id]=0
    #             return 0
    #
    #         right_path[node.id] = node.val + max(
    #             dfs(node.right, True, left_path, right_path),
    #             dfs(node.right, False, left_path, right_path),
    #         )
    #         return right_path[node.id]
    #
    #     # return node.val + max(dfs(node.left),dfs(node.right))
    #
    # if not root:
    #     return 0
    # # queue = deque()
    # # queue.append(root)
    # # queue.append(None)
    # # visited = {root.val}
    # # current_sum = 0
    # # max_path_sum = float('-inf')
    # left_path = dict()
    # right_path = dict()
    # dfs(root, True, left_path, right_path)
    # dfs(root, False, left_path, right_path)
    # print(left_path)
    # print(right_path)
    # path2sum = dict((i, left_path[i] + right_path[i]) for i in left_path.keys())
    # i = max(path2sum,key=path2sum.get)
    # return path2sum[i]
    # # maxPathSum = {}
    # # return root.val+max(left_path_sum, right_path_sum)
    # """
    # while queue:
    #     node = queue.popleft()
    #     if node:
    #         current_sum = node.val
    #
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     else:
    #         total = sum(node.val for node in queue)
    #         print(current_sum,total)
    #
    #         if total > max_path_sum:
    #             max_path_sum =total
    #         if queue:
    #             queue.append(None)
    #
    #
    # return max_path_sum
    # """
    max_path_sum = -1000000
    def find_max_path_sum(root):
        nonlocal max_path_sum
        if not root:
            return 0
        left = max(find_max_path_sum(root.left), 0)
        right = max(find_max_path_sum(root.right), 0)
        max_path_sum = max(max_path_sum, root.val+left + right)
        return root.val + max(left,right)

    find_max_path_sum(root)
    return max_path_sum





if __name__ == "__main__":
    root = TreeNode(6)
    insert(-10, root)
    insert(20, root)
    insert(-8, root)
    insert(9, root)
    insert(15, root)
    insert(7, root)
    print(num_nodes(root))

    inOrder(root)
    print("\n", numLeaves(root))
    printAtDepthK(root, 2)
    print("\n", largestValue(root))
    print(maxPathSum(root))
