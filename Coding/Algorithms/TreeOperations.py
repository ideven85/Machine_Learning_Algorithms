class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root,val):
    if not root:
        root = BinaryTree(val)
    if val==root.value:
        root=BinaryTree(val)
    elif val<root.value:
        root.left=insert(root.left,val)
    elif val>root.value:
        root.right=insert(root.right,val)
    return root


def rightSiblingTree(root):
    # Write your code here.
    pass
def flattenBinaryTree(root):
    # Write your code here.
    if not root:
        return None
    leftMost, _ = flattenTreeToDLL(root)
    return leftMost
def flattenTreeToDLL(root):
    if root.left is None:
        leftMost = root
    else:
        leftSubTreeLeftMost,leftSubTreeRightMost=flattenTreeToDLL(root.left)
        connectNodes(leftSubTreeRightMost,root)
        leftMost=leftSubTreeLeftMost
    if root.right is None:
        rightMost = root
    else:
        rightSubTreeLeftMost,rightSubTreeRightMost=flattenTreeToDLL(root.right)
        connectNodes(root,rightSubTreeLeftMost)
        rightMost=rightSubTreeRightMost
    return [leftMost,rightMost]



def connectNodes(left,right):
    left.right=right
    right.left=left
def flattenBinaryTreeToDLL(root,prev,head):
    if not root:
        return None
    flattenBinaryTreeToDLL(root.left,prev,head)
    root.left=prev
    if prev:
        prev.right=root
    head = root
    right=root.right
    head.left=root
    root.right=head
    prev=root

    flattenBinaryTreeToDLL(right,prev,head)

if __name__ == '__main__':
    bt = BinaryTree(10)
    insert(bt,5)
    insert(bt,8)
    insert(bt,12)
    head = flattenBinaryTree(bt)

    while head:
        print(head.value,end=' ')
        head=head.right
    print()