class Reverse:
    """
    Reverse Iterator
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


s = Reverse([1, 2, 3])
print(list(s))
