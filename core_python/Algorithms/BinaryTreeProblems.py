from collections import deque


class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, root, value):
        if not root:
            root = BinaryTree(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        return root

    def inOrder(self, root, lst):
        if root:
            self.inOrder(root.left, lst)
            # print(root.value,end=' ')
            lst.append(root.value)
            self.inOrder(root.right, lst)


"""
Function to return the sum of depths of all non leaf nodes
"""


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def allKindsOfNodeDepths(root: BinaryTree) -> int:
    # Write your code here.
    if root is None:
        return 0

    total = 0
    currentDepth = 0
    queue = deque()
    queue.append((root, currentDepth))
    while queue:
        node, depth = queue.pop()
        # print(depth)
        currentDepth += depth
        print(currentDepth)

        if not node.left and not node.right:
            total += currentDepth
            currentDepth = 0

        if node.left and node.right:
            queue.append((node.left, currentDepth + 1))
            queue.append((node.right, currentDepth + 1))

    return total


def rightSmallerThan(array):
    # Write your code here.
    n = len(array)
    if n == 0:
        return []
    # bt = BinaryTree(array[0])
    output = []
    for i in range(n):

        a = []
        bt = None
        bt = BinaryTree(array[i])
        for j in range(i + 1, n):
            bt.insert(bt, array[j])
            bt.inOrder(bt, a)
            print(a)
            output.append(a.index(array[i]))

        bt = None

    return output


if __name__ == "__main__":

    # print(allKindsOfNodeDepths(b))
    arr = [8, 5, 11, -1, 3, 4, 2]
    print(rightSmallerThan(arr))
