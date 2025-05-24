class LinkedList2:
    def __init__(self, element=None, next_node=None):
        if element:
            self.element = element
            self.next_node = LinkedList2(None)
            self.next_node = self
        else:
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
        if index == 0:
            return self.element
        else:
            self.next_node.get(index - 1)

    def set(self, index, value):
        # for _ in range(0,index-1):
        #     self=self.next_node
        # #self.element=value
        #
        # self.next_node=LinkedList2(value)
        # #self.next_node.next_node=None
        # self.element=value
        if index == 0:
            self.next_node = LinkedList2()
            self.element = value

        else:
            self.next_node.set(index - 1, value)


ll = LinkedList2(0)
print(ll.get(0))


ll.set(0, 12)
print(ll.get(0))
ll.set(1, "cat")
print(ll.get(1))
ll.set(1, "abc")
print(ll.get(1))
ll.set(2, 123)
print(ll.get(2))

print(ll)
