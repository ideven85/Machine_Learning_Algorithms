'''
@input -
node - root node of given tree
k = distance of nodes required
'''
from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.

    def printKDistantfromLeaf(self, root, k):
        output = deque()
        if not root:
            return 0
        output.append([root,0])
        while output:
            current, = output.popleft()




