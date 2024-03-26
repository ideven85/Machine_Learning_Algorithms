# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        # Write your code here
        self.root = {}

    def createSet(self, value):
        # Write your code here
        self.root[value] = value

    def find(self, value):
        # Write your code here
        if value not in self.root:
            return None
        else:
            if self.root[value] == value:
                return value
            else:
                while self.root[value] != value:
                    value = self.root[value]
        return value

    def union(self, valueOne, valueTwo):
        # Write your code here
        if valueOne not in self.root or valueTwo not in self.root:
            return
        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)
        if rootOne != rootTwo:
            self.root[rootOne] = rootTwo
