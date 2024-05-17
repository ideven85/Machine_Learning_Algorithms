class TrieNode:
    def __init__(self, value):
        self.value = value
        self.node = None
        self.is_terminating = False


class Trie:

    def __init__(self):
        self.is_terminating = False
        # self.prefix = TrieNode('\q')
        self.children = dict()

    def __setitem__(self, key, value):

        curr = self
        for char in key:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.is_terminating = value

    def insert(self, word: str) -> None:
        # __setitem__
        # if not word:
        #     return
        # curr = self
        # for char in word:
        #     if char not in curr.children:
        #         curr.children[char] = Trie()
        #     curr.children = curr.children[char]
        # curr.is_terminating = True
        return self.__setitem__(word, True)

    def __contains__(self, word: str):
        curr = self
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_terminating

    def search(self, word: str) -> bool:
        # __getitem__

        # curr = self
        # for char in word:
        #     if char not in curr.children:
        #         return False
        #     curr = curr.children[char]
        # return curr.is_terminating
        return self.__contains__(word)

    def startsWith(self, prefix: str) -> bool:
        # __contains__
        if not prefix:
            return False
        curr = self
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def __iter__(self):  # version A
        def helper(self, prefix):
            if self.is_terminating:
                yield prefix, self.value
            for letter, child in self.children.items():
                yield from helper(child, prefix + letter)

        return helper(self, "")


class WordDictionary:

    def __init__(self):

    def addWord(self, word: str) -> None:

    def search(self, word: str) -> bool:
        pass



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your Trie object will be instantiated and called as such:
word = 'apple'
prefix = 'apps'
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
print(trie.search("app"))  # return False
print(trie.startsWith("app"))  # return True
trie.insert("")
print(trie.search(""))  # return True
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# print(param_2)
# print(param_3)
