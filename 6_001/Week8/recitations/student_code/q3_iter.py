"""
Question 3: For each buggy implementation of the iter function below:
- What is going wrong?
- What changes do we need to make to fix the code, while keeping the same structure?
"""


class PrefixTree:
    def __init__(self):
        self.value = None
        self.children = {}

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key is not a string!")
        cur = self
        for char in key:
            if char not in cur.children:
                cur.children[char] = PrefixTree()
            cur = cur.children[char]
        cur.value = value



    # def __iter__(self):  # version A
    #     def helper(prefix,child=""):
    #         if self.value is not None:
    #             yield (prefix, self.value)
    #         for letter, child in self.children.items():
    #             helper(child, prefix + letter)
    #
    #     helper( "")

    def __iter__(self):  # version B


            for letter, subtree in self.children.items():
                if letter is None:
                    yield '',subtree.value
                if subtree.value is not None:
                    yield (letter + '', subtree.value)

                yield from [(letter + word, val) for word, val in subtree.__iter__()]


def test_tiny():
    import time

    expected = set(
        [
            ("", 0),
            ("bar", 1),
            ("bark", 2),
            ("bat", 3),
            ("cart", 4),
            ("cats", 5),
            ("at", 6),
        ]
    )
    start = time.perf_counter()
    t = PrefixTree()

    # set all the items
    t[""] = 0
    t["bar"] = 1
    t["bark"] = 2
    t["bat"] = 3
    t["cart"] = 4
    t["cats"] = 5
    t["at"] = 6
    # for key,val in t:
    #     print(key,val)
    # get all the items and make sure they are correct
    assert len(list(t)) == len(expected)
    result = set(t)
    assert result == expected
    end = time.perf_counter()
    print(f"test_tiny passed in {end-start} seconds")


def test_large():
    import time

    with open("words.txt", encoding="utf-8") as file:
        all_words = file.read().split("\n")

    expected = {word: i for i, word in enumerate(all_words)}
    start = time.perf_counter()
    # set all the words to their index in the all_words list
    t = PrefixTree()
    for i, word in enumerate(all_words):
        t[word] = i

    #assert len(list(t)) == len(all_words)
    assert dict(t) == expected
    end = time.perf_counter()
    print(f"test_large passed in {end-start} seconds")


# you can include test cases of your own in the block below.
if __name__ == "__main__":
    test_tiny()
    test_large()
