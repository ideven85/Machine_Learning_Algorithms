"""
Question 1: Review the code in test_tiny which creates a small PrefixTree t.
Draw a diagram to represent the structure of t.

Question 2: The implementation of __getitem__ and __setitem__ below is correct
but has many similarities. Refactor these functions to decrease
repetition while maintaining correctness. For an added bonus, try writing
the code iteratively to increase efficiency.
"""


class PrefixTree:
    def __init__(self):
        self.value = None
        self.children = {}

    def __setitem__(self, key, value):
        """
        Add a key with the given value to the prefix tree,
        or reassign the associated value if it is already present.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("Key is not a string!")
        curr = self
        for char in key:
            if char not in curr.children:
                curr.children[char] = PrefixTree()
            curr = curr.children[char]
        curr.value = value

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("Key is not a string!")
        # elif not key:
        #     if self.value is None:
        #         raise KeyError("Key does not have a value!")
        #     return self.value
        # elif key[0] not in self.children:
        #     raise KeyError("Key does not have a value!")
        # else:
        #     # return self.children[key[0]][key[1:]]
        #     return self.children[key[0]].__getitem__(key[1:])
        #
        curr = self
        for char in key:
            if char not in curr.children:
                raise KeyError("Key does not have a value")
            curr = curr.children[char]
        return curr.value


def test_tiny():
    import time

    word_vals = [
        ("bar", 1),
        ("bark", 2),
        ("bat", 3),
        ("cart", 4),
        ("cats", 5),
        ("at", 6),
    ]
    start = time.perf_counter()
    t = PrefixTree()
    # set all the items
    t["bar"] = 1
    t["bark"] = 2
    t["bat"] = 3
    t["cart"] = 4
    t["cats"] = 5
    t["at"] = 6
    # get all the items and make sure they are correct
    for word, val in word_vals:
        assert t[word] == val, f"{word} does not have value {val}"
    end = time.perf_counter()
    print(f"test_tiny passed in {end-start} seconds")


def test_large():
    import time

    with open("words.txt", encoding="utf-8") as file:
        all_words = file.read().split("\n")

    start = time.perf_counter()
    # set all the words to their index in the all_words list
    t = PrefixTree()
    for i, word in enumerate(all_words):
        t[word] = i

    # get all the items and make sure they are correct
    for i, word in enumerate(all_words):
        assert t[word] == i, f"{word} does not have value {i}"
    end = time.perf_counter()
    print(f"test_large passed in {end-start} seconds")


# you can include test cases of your own in the block below.
if __name__ == "__main__":
    test_tiny()
    test_large()


"""
Recursive:
q1_get_set.py::test_tiny PASSED                                          [ 50%]test_tiny passed in 1.2749998859362677e-05 seconds

q1_get_set.py::test_large PASSED                                         [100%]test_large passed in 0.15881274999992456 seconds


"""


"""
Iterative:
q1_get_set.py::test_tiny PASSED                                          [ 50%]test_tiny passed in 7.542003004346043e-06 seconds

q1_get_set.py::test_large PASSED                                         [100%]test_large passed in 0.09988620899821399 seconds

"""
