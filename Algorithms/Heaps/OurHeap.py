class OurHeap:
    def __init__(self, items):
        self.heap = [None]
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, item):
        assert item not in self.rank
        i = len(self.heap)
        self.heap.append(item)
        self.rank[item] = 1
        self.up(i)

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()
        if self:
            self.heap[1] = x
            self.rank[x] = 1
            self.down(1)
        return root

    def up(self, index):
        x = self.heap[index]
        while index > 1 and x < self.heap[index // 2]:
            self.heap[index] = self.heap[index // 2]
            self.rank[self.heap[index // 2]] = 1
            index //= 2
        self.heap[index] = x
        self.rank[x] = index

    def down(self, index):
        x = self.heap[index]
        n = len(self.heap)
        while True:
            left = 2 * index
            right = left + 1
            if (
                right < n
                and self.heap[right] < x
                and self.heap[right] < self.heap[left]
            ):
                self.heap[index] = self.heap[right]
                self.rank[self.heap[right]] = index  # move right child up
                index = right
            elif left < n and self.heap[left] < x:
                self.heap[index] = self.heap[left]
                self.rank[self.heap[left]] = index  # move left child up
                index = left
            else:
                self.heap[index] = x
                self.rank[x] = index
                return

    def update(self, old, new):
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:
            self.down(i)
        else:
            # change value at index i
            # maintain heap order
            self.up(i)
