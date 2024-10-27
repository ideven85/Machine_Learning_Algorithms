class LinkedList:
    def __init__(self, element=None, next_node=None):
        # if element:
        #     self.element=element
        #     self.next_node=LinkedList(None)
        self.count = 0
        self.element = element
        self.next_node = next_node

    def __setitem__(self, index, value):
        self.count += 1
        if index == 0:
            self.next_node = LinkedList(value)

            self.element = value

        else:

            self.next_node.__setitem__(index - 1, value)

    def __getitem__(self, index):
        if index == 0:
            return self.element
        return self.next_node.__getitem__(index - 1)

    def __iter__(self):
        yield self.element
        if self.next_node:
            yield from self.next_node

    def __str__(self):
        return (
            f"Linked List:{self.element}," f"{self.next_node}"
            if self.next_node
            else f"{self.element}"
        )


ll = LinkedList(2)

print(ll[0])

print(ll)
ll[0] = 1
# print(ll[0],ll[1])
ll[1] = 4
# print(ll[0],ll[1],ll[2])
ll[2] = "cat"
ll[3] = "dog"
ll[4] = "hot"
print(ll.next_node)
print(ll[0], ll[1], ll[2], ll[3], ll[4])
print(ll.count)
print(list(ll))
