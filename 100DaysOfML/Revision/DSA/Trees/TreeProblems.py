from collections import deque


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self,root:Node,val:int)->Node:
        if not root:
            root = Node(val)
        elif val<root.data:
            root.left = self.insert(root.left,val)
        elif val>=root.data:
            root.right = self.insert(root.right,val)
        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)

    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))

    def depth(self,root,node):
        if not root:
            return 0
        if root.data==node.data:
            return 0
        return 1+max(self.depth(root.left,node),self.depth(root.right,node))

    def check(self, root):
        #Code here
        queue=deque()
        queue.append([root,0])
        height = self.height(root)
        #print(height)
        depths = []
        count=0
        while queue:
            node,depth=queue.popleft()
            #depths.append(depth)
            if node:
                if not node.left and not node.right:
                    depths.append(depth)
                    count+=1


                queue.append([node.left,depth+1])
                queue.append([node.right,depth+1])
        if len(depths)==0:
            return True
        curr = depths[0]
        print(depths)
        print(count)
        for i in range(1,len(depths)):
            if depths[i]!=curr:
                return False

        return True

    paths = []
    def print_left_boundary(self,root):
        if not root: return
        if root.left:
            self.paths.append(root.data)
            self.print_left_boundary(root.left)
        elif root.right:
            self.paths.append(root.data)
            self.print_left_boundary(root.right)

    def print_leaf_nodes(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.paths.append(root.data)
        self.print_leaf_nodes(root.left)
        self.print_leaf_nodes(root.right)

    def print_right_boundary(self, root):
        if not root: return
        if root.right:
            self.print_right_boundary(root.right)
            self.paths.append(root.data)
        elif root.left:
            self.print_right_boundary(root.left)
            self.paths.append(root.data)


    def printBoundaryView(self,root):
        if not root:
            return self.paths
        self.paths.append(root.data)
        self.print_left_boundary(root.left)
        self.print_leaf_nodes(root.left)
        self.print_leaf_nodes(root.right)
        self.print_right_boundary(root.right)
        return self.paths

    def printBoundaryViewV1(self, root:Node)->None:
        paths = []
        node=root
        if not root:
            return
        #paths.append(node.data)
        while node:
            if node:
                paths.append(node.data)
                node = node.left

        node = root
        right_paths = []
        while node:
            node = node.right
            if node:
                right_paths.append(node.data)
        queue = deque()
        node=root
        queue.append(node)
        #print(paths)
        while queue:
            curr = queue.popleft()
            if curr:
                #print(curr.data)
                if not curr.left and not curr.right:
                    #print(curr.data)
                    if curr.data not in paths and curr.data not in right_paths:
                        paths.append(curr.data)
                queue.append(curr.left)
                queue.append(curr.right)
        right_paths=right_paths[::-1]
        #print(paths)
        #print(right_paths)
        # for path in paths:
        #     print(path,end=' ')
        paths.extend(right_paths)
        return paths
    def isSumProperty(self, root):
        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr:
                parent_sum = curr.data
                children_sum=0
                if not curr.left and not curr.right:
                    continue # Leaf Node

                if curr.left:
                    children_sum+=curr.left.data
                if curr.right:
                    children_sum+=curr.right.data
                #print(parent_sum, children_sum)
                if parent_sum!=children_sum:
                    return 0
                queue.append(curr.left)
                queue.append(curr.right)

        return 1



if __name__ == '__main__':
    root = Node(10)
    bst = BinarySearchTree()
    # bst.insert(root,10)
    # bst.insert(root,15)
    # bst.insert(root,6)
    # bst.insert(root,8)
    # bst.insert(root,7)
    # bst.insert(root,5)
    # bst.insert(root,13)
    # bst.insert(root,20)
    print(bst.height(root))
    bst.inorder(root)
    print()
    print(bst.check(root))
    print(bst.printBoundaryView(root))
    print(bst.isSumProperty(root))