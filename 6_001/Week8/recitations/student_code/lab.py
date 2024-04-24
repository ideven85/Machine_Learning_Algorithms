"""
COPY PASTE YOUR IMPLEMENTATION OF THE LAB HERE!
"""

# NO ADDITIONAL IMPORTS!
import doctest
from text_tokenize import tokenize_sentences


class PrefixTree:
    def __init__(self):
        self.value = None
        self.children = {}
        self._count = 0

    def __setitem__(self, key, value):
        """
        Add a key with the given value to the prefix tree,
        or reassign the associated value if it is already present.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("Dumbo")
        n = len(key)
        for i in range(n-1):
            if key[i] not in self.children:
                self.children[key[i]] = PrefixTree()
                # self.children[key[i]].value=None
                # Apparently if not key means after the last character
                print(self.value)
        self.children[key[n-1]]=PrefixTree()
        self.children[key[n-1]].value=value

    def __getitem__(self, key):
        """
        Return the value for the specified prefix.
        Raise a KeyError if the given key is not in the prefix tree.
        Raise a TypeError if the given key is not a string.
        """
        if not isinstance(key, str):
            raise TypeError("Dumbo")
        # elif not key:
        #     if not self.value:
        #         raise KeyError("Not present")
        #     return self.value
        # else:
        #     return self.children[key[0]][key[1:]]

        elif not key:
            if self.value is None:
                raise KeyError("Key not found")
            return self.value
        elif key[0] not in self.children:
            raise KeyError("Key not found")
        else:
            return self.children[key[0]].__getitem__(key[1:])

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
    #t["bar"] = 3
    #t["bark"] = ":)"
    #print(t._count)
    print(t["bat"])
