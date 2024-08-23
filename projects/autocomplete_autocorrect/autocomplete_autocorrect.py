"""
6.101 Lab:
Autocomplete
"""

# NO ADDITIONAL IMPORTS!
import doctest
import pickle
import os
from collections import Counter

LOCATION = os.path.realpath(os.path.dirname(__file__))
from text_tokenize import tokenize_sentences

# class TrieNode:
#     def __init__(self,data=None):
#         self.data=data
#         self.is_terminating=False
#         self.children=[TrieNode() for _ in range(26)]
#         self.child_count=0


# Basic Trie data structure customised without using TrieNode
# Started 15th April: 1:15 AM
# Map<
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
                raise KeyError("Key Not Found")

            return self
        elif value is None and key[0] not in self.children:
            raise KeyError("Key not found")
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

        curr = self
        for char in key:
            if char not in curr.children:
                curr.children[char] = PrefixTree()
            curr = curr.children[char]
        curr.value = value
        # elif not key:
        #     self.value=value
        # else:
        #     if key[0] not in self.children:
        #         self.children[key[0]]=PrefixTree()
        #     self.children[key[0]].__setitem__(key[1:],value)

        # self._get_node(key,value).value=value

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("The given word must be a string")
        elif not key:
            if self.value is None:
                raise KeyError("Key not found")
            return self.value
        elif key[0] not in self.children:
            raise KeyError("Key not found")
        else:
            return self.children[key[0]][key[1:]]
        # return self._get_node(key).value

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
        if not isinstance(key, str):
            raise TypeError("The given word must be a string")
        if key == "" and self.value is not None:
            return True

        elif not key:
            return self.value is not None
        elif key[0] not in self.children:
            return False
        else:
            return self.children[key[0]].__contains__(key[1:])

    # def print(self):
    #     current = self
    #     for letter,subtree in current.children.items():
    #
    #             print(letter,subtree.value)
    # def __iter__(self):  # version B
    #     for letter, subtree in self.children.items():
    #         # if subtree.value==0 or letter=='' or self.value==0:
    #         #     yield '',self.value
    #
    #         if not letter and self.value is not None:
    #             yield '',self.value
    #         if  subtree.value is not None:
    #             yield letter, subtree.value
    #
    #         yield from [(letter+word, val) for word, val in subtree.__iter__() ]
    def __iter__(self):  # version A
        def helper(self, prefix):
            if self.value is not None:
                yield (prefix, self.value)
            for letter, child in self.children.items():
                yield from helper(child, prefix + letter)

        return helper(self, "")

    # def __repr__(self):
    #     return f"{self.value}, {self.children}" if self.children else " Prefix Tree"

    # def __str__(self):
    #     return str(self.value)


def word_frequencies(text):
    """
    Given a piece of text as a single string, create a prefix tree whose keys
    are the words in the text, and whose values are the number of times the
    associated word appears in the text.
    """
    # raise NotImplementedError
    tokenised = tokenize_sentences(text)
    t = PrefixTree()

    words = ["" for _ in range(len(tokenised))]
    for i in range(len(tokenised)):
        words[i] = tokenised[i].split(" ")

    for i in range(len(words)):
        for word in words[i]:
            t[word] = 1 if word not in t else t[word] + 1

    return t


def autocomplete2(ptree, prefix, max_count=None):
    if not isinstance(prefix, str):
        raise TypeError

    all_words = [i for i in ptree if i[0].startswith(prefix)]

    if max_count is None:
        max_count = len(all_words)

    out_words = []
    for _ in range(max_count):
        best = (None, float("-inf"))
        for i in all_words:
            if i[1] > best[1] and i not in out_words:
                best = i
        if best != (None, float("-inf")):
            out_words.append(best)

    return [i[0] for i in out_words]


def autocomplete(tree, prefix, max_count=None):
    """
    Return the list of the most-frequently occurring elements that start with
    the given prefix.  Include only the top max_count elements if max_count is
    specified, otherwise return all.

    Raise a TypeError if the given prefix is not a string.
    """
    # raise NotImplementedError
    if not isinstance(prefix, str):
        raise TypeError("Prefix must be a string")
    if max_count == 0:
        return []
    # if prefix not in tree:
    #     raise KeyError("Prefix not present")
    # frequencies = list(word_frequencies(tree))
    # frequencies=list(tree)
    # print(prefix in tree)
    tree = list(tree)

    frequencies = [w for w in tree if w[0].startswith(prefix)]
    # print(frequencies)
    frequencies.sort(key=lambda x: x[1], reverse=True)

    # input("Check 1")

    out = [w for w, _ in frequencies]
    if not max_count:
        max_count = len(out)
    return out[:max_count]

    # if max_count:
    #     while max_count!=0:
    #
    #
    #
    #             if not frequencies:
    #                 return out
    #             if not max_count:
    #                 break
    #             #input(word)
    #             if prefix in word:
    #                 #input("True")
    #                 out.append(word)
    #                 max_count-=1
    #
    #
    #         if not frequencies:
    #                 return out
    #
    # else:
    #     for word in frequencies:
    #         if prefix in word:
    #             out.append(word)
    # return out


def levenshteinDistance(str1, str2):
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
            elif j < n and i < m and str1[i - 1] == str2[j] and str1[i] == str2[j - 1]:
                L[i][j] = L[i - 1][j - 1]
            else:
                L[i][j] = 1 + min(L[i - 1][j], L[i - 1][j - 1], L[i][j - 1])

    return L[-1][-1]


# def edit_results(word1,word2):
#     n = len(word1)
#     m = len(word2)
#
#     if n-m>1:
#         return False
#     # Operations -> Insert,Delete,Edit,Transpose adjacent characters
#     dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             diff = ord(word1[i])-ord(word2[j])
#             dp[i][j]


def autocorrect(tree, prefix, max_count=None):
    """
    Return the list of the most-frequent words that start with prefix or that
    are valid words that differ from prefix by a small edit.  Include up to
    max_count elements from the autocompletion.  If autocompletion produces
    fewer than max_count elements, include the most-frequently-occurring valid
    edits of the given word as well, up to max_count total elements.
    """
    # raise NotImplementedError
    if max_count == 0:
        return []
    completions = autocomplete(tree, prefix, max_count)
    corpus = list(tree)
    # print(corpus)
    if max_count and len(completions) == max_count:
        return completions
    diff = 0
    if max_count:
        if len(completions) < max_count:
            diff = max_count - len(completions)
        else:
            diff = 0
    else:
        diff = len(corpus) - len(completions)
    print(diff)
    corpus.sort(key=lambda x: x[1], reverse=True)

    for word, _ in corpus:
        if diff:
            if levenshteinDistance(prefix, word) == 1:
                if not diff:
                    break
                if word not in completions:
                    completions.append(word)
                diff -= 1
    return completions


# todo
def word_filter(tree, pattern):
    """
    Return list of (word, freq) for all words in the given prefix tree that
    match pattern.  pattern is a string, interpreted as explained below:
         * matches any sequence of zero or more characters,
         ? matches any single character,
         otherwise char in pattern char must equal char in word.
    """
    raise NotImplementedError


def dictify(t):
    assert set(t.__dict__) == {
        "value",
        "children",
    }, "PrefixTree instances should only contain the two instance attributes mentioned in the lab writeup."
    out = {"value": t.value, "children": {}}
    for ch, child in t.children.items():
        out["children"][ch] = dictify(child)
    return out


def from_dict(d):
    t = PrefixTree()
    for k, v in d.items():
        t[k] = v
    return t


# you can include test cases of your own in the block below.
if __name__ == "__main__":
    t = PrefixTree()
    t[""] = 3
    t["bat"] = 7
    t["bar"] = 3
    t["bark"] = "-)"
    t["bat"] = 2

    t["bank"] = 4
    t["ban"] = 7

    # t.print()

    # print(t[""])

    # with open('texts/dracula.txt','r') as f:
    #     ALL_WORDS=f.read()
    # #print(ALL_WORDS.split("\n")[:5])
    #
    # with open('testing_data/6.pickle','rb') as f:
    #     first=pickle.load(f)
    # #print(type(first))
    # #print(first)
    # l=word_frequencies(
    #     "toonces was a cat who could drive a car very fast until he crashed."
    # )
    #
    # l1=word_frequencies(ALL_WORDS)
    # words = "bat bat bark bar bank ban band"
    # tree=word_frequencies(words)
    #
    #
    # #print(list(l1)[:10])
    # print("AutoComplete Test 1:")
    # print(autocomplete(tree,"ban",2))
    words = "cats cattle hat car act at chat crate act car act at car hat"
    # print(Counter(words.split(' ')))
    t = word_frequencies(words)
    result1 = autocomplete(t, "cat", 4)
    print(result1)
    result = autocorrect(t, "cat", 4)
    print(result)
    # print(levenshteinDistance("cat","act"))
    alphabet = a = "abcdefghijklmnopqrstuvwxyz"

    word_list = [
        "aa" + l1 + l2 + l3 + l4 for l1 in a for l2 in a for l3 in a for l4 in a
    ]
    word_list.extend(["apple", "application", "apple", "apricot", "apricot", "apple"])
    word_list.append("bruteforceisbad")

    t = word_frequencies(" ".join(word_list))
    print(list(t))
    for i in range(50):
        result1 = autocomplete2(t, "ap", 1)
        result2 = autocomplete2(t, "ap", 2)
        result3 = autocomplete2(t, "ap", 3)
        result4 = autocomplete2(t, "ap")
        result5 = autocomplete2(t, "b")
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
