# Feel free to add new properties and methods to the class.
class MinMaxStack:

    root = []

    def peek(self):
        # Write your code here.
        return self.root[len(self) - 1]

    def __len__(self):
        return len(self.root)

    def pop(self):
        # Write your code here.
        if len(self) > 0:
            return self.root.pop()

    def push(self, number):
        # Write your code here.
        self.root.insert(0, number)

    def getMin(self):
        # Write your code here.
        return min(self.root)

    def getMax(self):
        # Write your code here.
        return max(self.root)


if __name__ == "__main__":
    stack = MinMaxStack()
    stack.push(5)
    print(stack.getMin())
    print(stack.getMax())
    print(stack.peek())
    stack.push(2)
    stack.push(7)
    print(stack.getMin())
    print(stack.getMax())
