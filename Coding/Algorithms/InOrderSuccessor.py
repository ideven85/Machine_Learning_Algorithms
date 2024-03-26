class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(root: BinaryTree, node: BinaryTree):
    # Write your code here.
    if root is None:
        return None
    if node.right:
        return findLeftMostNodeInRight(node.right)
    else:
        q = node
        x = node.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x


def findLeftMostNodeInRight(root: BinaryTree):
    while root.left:
        root = root.left
    return root
