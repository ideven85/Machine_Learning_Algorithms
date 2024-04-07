"""
1) 1) What is an iterable? An iterator? A generator? What are the similarities and
differences between them?
"""

# Doubt exactly what a generator object is because java does not have generators, but generators
# are used to stopping iteration and giving current element, like say in Java, IntStream.rangeClosed(1,100).parallel.filter(x->x%2!=0).peek()
# Peek is an intermediary operation not a terminal operation in streams in Java, in Python I cannot describe exactly what it means

"""
Iterable is an object which we can iterate over
Iterator is an object which iterates over an iterable
Generators are objects which yield the current element # Not clear Need practice
"""


"""
2) How do you make an iterator "from an iterable object in Python?"
Calling next with a generator passed in will cause Python to start running the body of the code, 
run until we see a yield, pause the execution again, and give us the value that was yielded from the generator.
Object is already iterable... either by implementing __iter__ or "__getitem_- which fetches bu in index"
 
"""

class Stack:
    def __init__(self):
        self._stack = []
        self._length = 0


    def push(self,item):
        self._stack.append(item)
        self._length+=1

    def pop(self):

        try:
            self._length-=1
            return str(self._stack.pop(0))
        except IndexError as e:
             print("Stack is empty, please add some more elements before pooping",e)




    def __iadd__(self, item):
        self.push(item)
    def __len__(self):
        return self._length


    def __getitem__(self, index):
        if len(self):
           return self._stack[index]
        else:
            raise EmptyException("Stack is Empty")


    def __iter__(self):
        if len(self):
           return self._stack[-1]
        else:
            raise StopIteration("Add more elements to me please")
    def __repr__(self):
        return ' '.join(str(x) for x in self._stack)


    # def __str__(self):
    #     return self._stack
class EmptyException(Exception):
    pass


if __name__ == '__main__':

    obj = Stack()
    obj.push(1)
    obj.push(2)
    # obj+=[2]
    print(obj)

    for i in range(len(obj)):
        print(obj[i], end=' ')
    print()
    for val in obj:
        print(val)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop()) # Error

