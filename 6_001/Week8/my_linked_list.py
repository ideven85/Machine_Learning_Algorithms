class LinkedList:
    class Node:
        """Lightweight, nonpublic

        class for storing a singly linked node.
        """

        slots = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size=0

    def __len__(self):
        return self._size
    def insert(self,value):
        if not len(self):
            self._head=self.Node(value,self._head)
            self._head._next=None
            self._size+=1
        else:
            current=self._head
            #print(len(self))
            for _ in range(len(self)-1):
                #print(current._element)
                current=current._next

            current._next=self.Node(value,current._next)
            #print(current._next._element)
            current=current._next
            current._next=None
            self._size+=1
    def __iter__(self):
        current=self._head
        while current :
            yield current._element
            current=current._next



a=LinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
print(list(a))

