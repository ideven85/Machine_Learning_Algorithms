class LinkedList:
    def __init__(self,element,next_node=None):
        self.element = element
        self.next_node = next_node

    def get(self,index):
        if index==0:
            return self.element
        if self.next_node is None:
            raise IndexError(f"{index} out of bounds")
        return self.next_node.get(index-1)

    def set(self,index,value):
        if index==0:
            self.element=value
        if self.next_node is None:
            raise IndexError(f"{index} out of bounds")
        self.next_node.set(index-1,value)

    def __repr__(self):
        return f"LinkedList({self.element}, {self.next_node})"
a = LinkedList(4,
          LinkedList(8,
              LinkedList(15,
                  LinkedList(16,
                      LinkedList(23, LinkedList(42))))))
print(a)


class LinkedList_Refactored:
    class _Node:
        def __init__(self,value=0):
            self.value=value
            self.next_node=None
        def __repr__(self):
            return str(self.value) + " "
    def __init__(self,value=0):
        self.value=self._Node(value).value
        self.next_node=self._Node().next_node
        #self.next_node.next_node=None
        self.length=0

    # def __getstate__(self):
    #     return self.element
    # def _get_node(self,index):
    #     if  index==0:
    #         return self.element
    #     elif self.next_node is None:
    #         raise IndexError(f"{index} out of bounds")
    #     else:
    #         return self.next_node._get_node(index-1)
    #
    def get(self,index):
        if not len(self):
            return 0
        if index==0:
            return self.next_node.value
        if 0<index<len(self):
            current=self.next_node
            for _ in range(index):
                print(current.value)
                current=current.next_node
            return current.value
        else:
            raise IndexError(f"{index} should be between 0 and {len(self)}")

    def set(self,index,value):
        if not self.next_node:
            self.next_node=self._Node(value)
        current = self.next_node
        for _ in range(index):
            current = current.next_node

        current= self._Node(value)
        current.next_node=None
        self.length+=1

    def __len__(self):
        return self.length
    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set(index, value)

    # def __iter__(self):
    #     current = self
    #     while current:
    #         yield current.element
    #         current=current.next_node

    def __iter__(self):
        current=self.next_node
        for _ in range(len(self)):
            yield self.next_node.value  # same as: yield from self.next_node.__iter__()




a=LinkedList_Refactored()
a[0]=3
a[1]=4
a[2]=5
print(len(a))
print(a[1])
print(list(a))
