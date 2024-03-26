class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root: BST, value):
    if not root:
        root = BST(value)
    elif root.value == value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def inOrder(root: BST):
    if root:
        inOrder(root.left)
        print(root.value, end=" ")
        inOrder(root.right)


def findClosestValueInBst(tree: BST, target: int) -> int:
    # Write your code here.
    value = -float("inf") if target > 0 else float("inf")
    return closestValueUtil(tree, target, value)


def closestValueUtil(root: BST, target: int, value):
    if root is None:
        return value
    if root.value == target:
        return root.value
    if abs(root.value - target) <= abs(value - target):
        value = root.value
    if target < root.value:
        return closestValueUtil(root.left, target, value)
    else:
        return closestValueUtil(root.right, target, value)


def validateBst(root: BST) -> bool:
    # Write your code here.
    minimum = -float("inf")
    maximum = float("inf")
    return validateBinarySearchTree(root, minimum, maximum)


def validateBinarySearchTree(root, minimum, maximum):
    if root is None:
        return True
    return (
        minimum <= root.value < maximum
        and validateBinarySearchTree(root.left, minimum, root.value)
        and validateBinarySearchTree(root.right, root.value, maximum)
    )


class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None
        self.leftSubTree = None


class RightSmallerBST:

    def __init__(self, value, index, smallerAtInsert):
        self.value = value
        self.index = index
        self.smallerAtInsert = smallerAtInsert
        self.leftSubTreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, index, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubTreeSize += 1
            if self.left is None:
                self.left = RightSmallerBST(value, index, numSmallerAtInsertTime)
            else:
                self.left.insert(value, index, numSmallerAtInsertTime)
        else:
            # print(self.leftSubTreeSize,end=' ')
            numSmallerAtInsertTime += self.leftSubTreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
                if self.right is None:
                    self.right = RightSmallerBST(value, index, numSmallerAtInsertTime)
                else:
                    self.right.insert(value, index, numSmallerAtInsertTime)


def rightSmallerThan(array):
    # Write your code here.[8, 5, 11, -1, 3, 4, 2]
    n = len(array)
    output = [0 for _ in range(n)]
    if sorted(array) == array:
        return output
    # specialBST = RightSmallerBST()
    for i in range(n):
        if i == n - 1:
            output[i] = 0
            break
        x = array[i + 1 :]
        x.sort()
        # print(x)
        current = array[i]
        count = 0
        j = 0
        while j < len(x) and x[j] < current:
            count += 1
            j += 1
        output[i] = count
    return output


def rightSmallerArray(array):
    if len(array) == 0:
        return []
    lastIndex = len(array) - 1
    bst = RightSmallerBST(array[lastIndex], lastIndex, 0)
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i)
    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts


def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.index] = bst.smallerAtInsert
    # print(rightSmallerCounts)
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)


def rightSmallerArraySecond(array):
    if array is None:
        return []
    counts = array[:]
    n = len(array)
    bst = SpecialisedBST(counts[n - 1])
    counts[n - 1] = 0
    for i in reversed(range(n - 1)):
        bst.insert(array[i], i, counts)
    return counts


class SpecialisedBST:
    def __init__(self, value):
        self.value = value
        self.leftSubTreeSize = 0
        self.left = None
        self.right = None

    def insert(self, value, index, rightSmallerCounts, numSmallerAtInsertTime=0):
        if value < self.value:
            self.leftSubTreeSize += 1
            if self.left is None:
                self.left = SpecialisedBST(value)
                rightSmallerCounts[index] = numSmallerAtInsertTime

            else:
                self.left.insert(
                    value, index, rightSmallerCounts, numSmallerAtInsertTime
                )
        else:
            numSmallerAtInsertTime += self.leftSubTreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
                if self.right is None:
                    self.right = SpecialisedBST(value)
                    rightSmallerCounts[index] = numSmallerAtInsertTime
                else:
                    self.right.insert(
                        value, index, rightSmallerCounts, numSmallerAtInsertTime
                    )


def invertBinaryTree(root):
    if root:
        invertBinaryTree(root.left)
        invertBinaryTree(root.right)
        root.left, root.right = root.right, root.left
    return root


if __name__ == "__main__":
    root = BST(10)
    insert(root, 15)
    insert(root, 6)
    insert(root, 12)
    insert(root, 13)
    print(findClosestValueInBst(root, 8))
    inOrder(root)
    print(validateBst(root))
    a = [8, 5, 11, -1, 3, 4, 2]
    print()
    # print(rightSmallerThan(a))
    print(rightSmallerArray(a))
    print(rightSmallerArraySecond(a))
