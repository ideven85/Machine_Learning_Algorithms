from os import *
from sys import *
from collections import *
from math import *


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def largestBST(root):
    # Write your code here.
    if not root:
        return 0

    queue = deque()
    size = 0
    max_size = 0
    queue.append([root, root.data])
    while queue:
        flag = True
        current, value = queue.popleft()
        if current.left and current.right:
            if current.left.data < value < current.right.data:
                size += 1
            else:
                size = 0

            queue.append([current.left, value])
            queue.append([current.right, value])
        elif current.left:
            if current.left.data < value:
                size += 1
            else:
                size = 0
            queue.append([current.left, value])
        elif current.right:
            if current.right.data > value:
                size += 1
            else:
                size = 0
            queue.append([current.right, value])

        if max_size < size:
            max_size = size
