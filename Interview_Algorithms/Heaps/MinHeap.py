# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        n = len(array)
        mid = (len(array) - 2) // 2
        for i in reversed(range(mid + 1)):
            self.siftDown(i, n - 1, array)
        return array

    def siftDown(self, currentIndex, endIndex, heap):
        # Write your code here.
        leftChild = currentIndex * 2 + 1
        childIndex = -1
        while leftChild <= endIndex:
            rightChild = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1

            if rightChild != -1 and heap[rightChild] < heap[leftChild]:
                childIndex = rightChild
            else:
                childIndex = leftChild
            if heap[currentIndex] > heap[childIndex]:
                heap[currentIndex], heap[childIndex] = heap[childIndex], heap[currentIndex]
                currentIndex = childIndex
                leftChild = currentIndex * 2 + 1
            else:
                return

    def __len__(self):
        return len(self.heap)

    def siftUp(self, childIndex):
        # Write your code here.
        parentIndex = (childIndex - 1) // 2
        while childIndex > 0 and self.heap[childIndex] < self.heap[parentIndex]:
            self.heap[childIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[childIndex]

            childIndex = parentIndex
            parentIndex = (childIndex - 1) // 2

    def peek(self):
        # Write your code here.
        if len(self) > 0:
            return self.heap[0]

    def remove(self):
        # Write your code here.
        self.heap[0], self.heap[len(self) - 1] = self.heap[len(self) - 1], self.heap[0]
        answer = self.heap.pop()
        self.siftDown(0, len(self) - 1, self.heap)#
        return answer

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self) - 1)


if __name__ == '__main__':
    a=[48, 12, 24, 7, 8,  24, 391, 24, 56, 2, 6, 8, 41]
    heap = MinHeap(a)
    print(a)
    print(heap.peek())
    heap.insert(5)
    print(heap.peek())
    print(heap.remove())
    print(heap.remove())
