import pytest
import pickle
import lab
import os

TEST_DIRECTORY = os.path.dirname(__file__)


# convert prefix tree into a dictionary...
def dictify(t):
    assert set(t.__dict__) == {
        "value",
        "children",
    }, "PrefixTree instances should only contain the two instance attributes mentioned in the lab writeup."
    out = {"value": t.value, "children": {}}
    for ch, child in t.children.items():
        out["children"][ch] = dictify(child)
    return out


# ...and back
def from_dict(d):
    t = lab.PrefixTree()
    for k, v in d.items():
        t[k] = v
    return t


# make sure the keys are not explicitly stored in any node
def any_key_stored(tree, keys):
    keys = [tuple(k) for k in keys]
    for i in dir(tree):
        try:
            val = tuple(getattr(tree, i))
        except:
            continue
        for j in keys:
            if j == val:
                return repr(i), repr(j)
    for child in tree.children:
        if len(child) != 1:
            return repr(child), repr(child)
    for child in tree.children.values():
        key_stored = any_key_stored(child, keys)
        if key_stored:
            return key_stored
    return None


# read in expected result
def read_expected(fname):
    with open(os.path.join(TEST_DIRECTORY, "testing_data", fname), "rb") as f:
        return pickle.load(f)


import doctest
from text_tokenize import tokenize_sentences


# Basic Huffman Encoding Technique customised
# Started 15th April: 1:15 AM
class PrefixTree:

    # class _Node:
    #     def __init__(self,value=None,next_node=None):
    #         self.value=value
    #         self.next_node=next_node
    #
    #     def __str__(self):
    #         return f"{self.value}"
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

    # def _get_node(self, index, value):
    #     if index==0:
    #         self.element=value
    #     else:
    #         self.children._get_node(index-1,value)=

    def __setitem__(self, key, value):
        """
        Add a key with the given value to the prefix tree,
        or reassign the associated value if it is already present.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("The given key must be a string")
        n = len(key)

        for i in range(n - 1):

            if key[i] in self.children:
                continue
            self.children[key[i]] = self.value
        # todo Reassign value of bark to 3 and bar to 3

        self.children.setdefault(key[n - 1], value)

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("The given word must be a string")
        if self.children[key] is None:

            raise KeyError("Given word not found")
        else:
            # print(self.children[key])
            return self.children[key]

    def __delitem__(self, key):
        """
        Delete the given key from the prefix tree if it exists.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        raise NotImplementedError

    def __contains__(self, key):
        """
        Is key a key in the prefix tree?  Return True or False.
        Raise a TypeError if the given key is not a string.
        """
        raise NotImplementedError

    def __iter__(self):
        """
        Generator of (key, value) pairs for all keys/values in this prefix tree
        and its children.  Must be a generator!
        """
        raise NotImplementedError


if __name__ == "__main__":

    t = PrefixTree()
    t["cat"] = 0
    t["car"] = 1
    t["carpet"] = 2

    expect = read_expected("2.pickle")

    print(expect)
