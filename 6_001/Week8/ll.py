class LinkedList2:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node

    # def get(self,index):
    #     for _ in range(index):
    #         self=self.next_node
    #     return self.element

    # def _get_node(self, index):
    #     if index == 0:
    #         return self
    #     elif self.next_node is None:
    #         raise IndexError("Index out of bounds")
    #     else:
    #         self.next_node._get_node(index - 1)

    def get(self, index):
        for _ in range(index):
            self = self.next_node
        return self.element

    def set(self, index, value):

        for _ in range(index):
            self = self.next_node
        self.next_node = LinkedList2(value)

    # self.next_node.element=value


ll = LinkedList2(4)
print(ll.get(0))

ll.set(0, 12)

print(ll.get(0))
ll.set(0, "cat")
print(ll.get(0))
ll.set(1, "abc")
print(ll.get(1))
