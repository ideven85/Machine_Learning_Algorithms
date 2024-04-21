"""
6.101 Lab:
Autocomplete
"""

# NO ADDITIONAL IMPORTS!
import doctest
from text_tokenize import tokenize_sentences


# Basic Huffman Encoding Technique customised
# Started 15th April: 1:15 AM
#Map<
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


    def set(self,index,key,value):
        character=ord(key[index])-ord('a')
        if index == len(key)-1:
            self.children[index]=PrefixTree()
            self.children[ord(key[index])-ord('a')]=value


        else:
            if character not in self.children:
                self.children[character]=PrefixTree()
                self.children[character].value=None

            #self.children.setdefault(key[index],PrefixTree())

            #print(self.children)
            #self.children=self.children.children

            self.set(index+1,key,value)




    def __setitem__(self, key, value):
        """
        Add a key with the given value to the prefix tree,
        or reassign the associated value if it is already present.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("The given key must be a string")
        n = len(key)
        flag = False
        self.set(0,key,value)




    def __getitem__(self, key):
        print(self.children)
        """
        Return the value for the specified prefix.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("The given word must be a string")
        character = ord(key[len(key)-1])-ord('a')
        if self.children[character] is None:

            raise KeyError("Given word not found")
        else:
            # print(self.children[key])
            return self.children[ord(key[len(key)-1])-ord('a')]

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

    def __str__(self):
        return str(self.value)
def word_frequencies(text):
    """
    Given a piece of text as a single string, create a prefix tree whose keys
    are the words in the text, and whose values are the number of times the
    associated word appears in the text.
    """
    raise NotImplementedError


def autocomplete(tree, prefix, max_count=None):
    """
    Return the list of the most-frequently occurring elements that start with
    the given prefix.  Include only the top max_count elements if max_count is
    specified, otherwise return all.

    Raise a TypeError if the given prefix is not a string.
    """
    raise NotImplementedError


def autocorrect(tree, prefix, max_count=None):
    """
    Return the list of the most-frequent words that start with prefix or that
    are valid words that differ from prefix by a small edit.  Include up to
    max_count elements from the autocompletion.  If autocompletion produces
    fewer than max_count elements, include the most-frequently-occurring valid
    edits of the given word as well, up to max_count total elements.
    """
    raise NotImplementedError


def word_filter(tree, pattern):
    """
    Return list of (word, freq) for all words in the given prefix tree that
    match pattern.  pattern is a string, interpreted as explained below:
         * matches any sequence of zero or more characters,
         ? matches any single character,
         otherwise char in pattern char must equal char in word.
    """
    raise NotImplementedError


# you can include test cases of your own in the block below.
if __name__ == "__main__":
    t = PrefixTree()
    t["bat"] = 7
    t["bark"] = "-)"
    print(len(t.children))
    t["bar"] = 3
    # print(t["bark"])
    # print(t["bat"])
    # print(t['bark'])
