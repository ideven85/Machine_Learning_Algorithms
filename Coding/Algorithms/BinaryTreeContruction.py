# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        # Write your code here.

        if value < self.value:
            if not self.left:
                return False
            return self.left.contains(value)

        elif value > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right:

                self.right.remove(value, self)
        else:
            if self.left and self.right:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
        return self

    def getMinValue(self):
        if not self.left:
            return self.value
        else:
            return self.left.getMinValue()


if __name__ == "__main__":
    root = BST(10)
    root.insert(15)
    root.insert(20)
    root.insert(12)
    root.insert(17)
    root.insert(5)
    root.insert(7)
    root.insert(3)

    print(root.contains(12))
    root.remove(10)
    print(root.contains(10))
