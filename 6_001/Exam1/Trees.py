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

    return find_max_path_sum(root)


def find_max_path_sum(
    root,
):  # Memory Usage is how many frames that are at each recursive call
    max_path_sum = 0
    if not root:
        return 0
    left = max(find_max_path_sum(root.left), 0)
    right = max(find_max_path_sum(root.right), 0)
    max_path_sum = max(max_path_sum, root.val + left + right)
    print(max_path_sum, end=" ")
    return root.val + max(left, right)


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
