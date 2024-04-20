class LinkedList:
    def __init__(self,element=None,next_node=None):
        # if element:
        #     self.element=element
        #     self.next_node=LinkedList(None)

        self.element=element
        self.next_node=next_node

    def __setitem__(self, index, value):
        if index==0:
            self.next_node=LinkedList(value)
            self.element=value

        self.next_node.__setitem__(index-1,value)

    def set(self,index,value):
    def __getitem__(self, index):
        if index==0:
            return self.element
        return self.__getitem__(index-1)


ll = LinkedList(2)

# print(ll[0])

ll[0]=3

# print(ll[0],ll[1])
ll[1]=4
# print(ll[0],ll[1],ll[2])
ll[2]='cat'
ll[3]='dog'
ll[4]='hot'
print(ll[4])