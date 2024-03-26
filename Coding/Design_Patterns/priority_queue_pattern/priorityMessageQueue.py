from .message import Message


class PriorityMessageQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) <= 0

    def addMessage(self, message: Message) -> None:
        self.queue.append(message)
        self.size += 1
        self.maxHeapifyUp()

    def removeMessage(self):
        if self.is_empty():
            return None
        root = self.queue.pop(0).message
        self.size -= 1
        self.maxHeapifyDown()
        return root

    def maxHeapifyUp(self):
        childIndex = len(self.queue) - 1
        parentIndex = (childIndex - 1) // 2
        while childIndex > 0:
            child = self.queue[childIndex]
            parent = self.queue[parentIndex]
            if child.priority > parent.priority:
                self.queue[childIndex], self.queue[parentIndex] = parent, child
                childIndex = parentIndex
                parentIndex = (childIndex - 1) // 2
            else:
                return

    def maxHeapifyDown(self):
        parentIndex = 0
        childIndex1 = 1
        childIndex2 = 2
        while childIndex2 < len(self) and (
            self.queue[parentIndex].priority <= self.queue[childIndex1].priority
            or self.queue[parentIndex].priority <= self.queue[childIndex2].priority
        ):

            minIndex = None
            if self.queue[childIndex1].priority >= self.queue[childIndex2].priority:
                minIndex = childIndex1
            else:
                minIndex = childIndex2
            self.queue[parentIndex], self.queue[minIndex] = (
                self.queue[minIndex],
                self.queue[parentIndex],
            )
            parentIndex = minIndex
            childIndex1 = parentIndex * 2 + 1
            childIndex2 = childIndex1 + 1
