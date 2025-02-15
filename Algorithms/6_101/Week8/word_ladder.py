import time
from collections import defaultdict
from typing import List


class PrefixTree:

    def __init__(self):
        """
                The __init__ method takes no arguments. It should set up exactly two instance variables:

        value, the value associated with the sequence ending at this node.
         Initial value is None (we will assume that a value of None means that a given key has no value associated with it,
         not that the value None is associated with it).

        children, a dictionary mapping a single-element sequence (in our case, a length-1 string)
         to another node, i.e., the next level of the prefix-tree hierarchy (prefix trees are a recursive data structure).
          Initial value is an empty dictionary.


        """
        self.value = None
        self.children = dict()
        # self.is_terminating=False
        # self.data = []

    # package default function
    def _get_node(self, key, value=None):
        if not isinstance(key, str):
            raise TypeError("Word Must Be a string")

        if not key:

            if not value and not self.value:
                return None

            return self
        elif value is None and key[0] not in self.children:
            return None
        elif value and key[0] not in self.children:

            self.children[key[0]] = PrefixTree()
        return self.children[key[0]]._get_node(key[1:], value)

    def __setitem__(self, key, value):
        """
        Add a key with the given value to the prefix tree,
        or reassign the associated value if it is already present.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("Word Must Be a string")

        self._get_node(key, value).value = value

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """

        return self._get_node(key).value

    def __delitem__(self, key):
        """
        Delete the given key from the prefix tree if it exists.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        self._get_node(key).value = None

    def __contains__(self, key):
        """
        Is key a key in the prefix tree?  Return True or False.
        Raise a TypeError if the given key is not a string.
        """

        return self._get_node(key) is not None

    def __iter__(self):  # version A
        def helper(self, prefix):

            if self.value is not None:
                yield prefix, self.value
            for letter, child in self.children.items():
                yield from helper(child, prefix + letter)

        return helper(self, "")

    #
    # def __next__(self):
    #     for letter,subtree in self.children.items():
    #

    def __repr__(self):
        return f"{self.value}, {self.children}" if self.children else " Prefix Tree"

    # def __str__(self):
    #     return str(self.value)


class Solution:

    characters = [0 for _ in range(26)]
    mapping = defaultdict(list)

    # def distance(self, s1, s2):
    #     count = 0
    #     for index, char in enumerate(s1):
    #         temp = ord(char) - ord("a")
    #         self.characters[temp] += 1
    #     for char in s2:
    #         temp = ord(char) - ord("a")
    #
    #         if self.characters[temp]:
    #             self.characters[temp] -= 1
    #             count += 1
    #     return count

    def levenshteinDistance(self, str1, str2):
        # Write your code here.
        m = len(str1)
        n = len(str2)
        L = [[i for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            L[i][0] = L[i - 1][0] + 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    L[i][j] = L[i - 1][j - 1]

                else:
                    L[i][j] = 1 + min(L[i - 1][j], L[i - 1][j - 1], L[i][j - 1])

        return L[-1][-1]

    graph = defaultdict(list)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Given two words, beginWord and endWord,
        and a dictionary wordList,
        return the number of words in the shortest transformation sequence from beginWord to endWord,
        or 0 if no such sequence exists.
        @param beginWord:
        @param endWord:

        """
        if endWord not in wordList:
            return 0
        for word in wordList:
            distance = self.levenshteinDistance(beginWord, word)
            self.graph[word].append((word, distance))

        agenda = [(beginWord,)]
        count = 1
        while agenda:
            current = agenda.pop()
            if self.levenshteinDistance(current, endWord) == 1:
                count += 1
                return count


beginWord = "hit"
endWord = "cog"

wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

sol = Solution()
s = time.perf_counter_ns()
print(sol.ladderLength(beginWord, "cog", wordList))
end = time.perf_counter_ns()
print(end - s)  # 0.20331937499940977
