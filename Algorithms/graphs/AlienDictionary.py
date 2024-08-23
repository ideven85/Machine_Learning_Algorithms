from collections import defaultdict
from typing import List


# todo
class AlienDictionary:

    graph = defaultdict(list)

    dictionary = [0 for _ in range(26)]

    def alienOrder(self, words: List[str]) -> str:
        """
                You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
        sorted lexicographically
         by the rules of this new language.
         Approach: Using Topological Sorting
         Dictionary contains only lowercase letters
        """
        output = str()
        for word in words:

            for char in word:
                self.dictionary[ord(char) - ord("a")] += 1

        print(self.dictionary)

        return output


if __name__ == "__main__":
    """


    Example 1:

    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"
    """
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(AlienDictionary().alienOrder(words))
