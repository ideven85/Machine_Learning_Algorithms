from collections import Counter
from copy import deepcopy


def isIsomorphic(s: str, t: str) -> bool:
    map1 = [0 for _ in range(256)]
    map2 = [0 for _ in range(256)]
    for i in range(len(s)):
        char1 = ord(s[i])
        char2 = ord(t[i])
        if map1[char1 - ord("a")] != map2[char2 - ord("a")]:
            return False
        map1[char1 - ord("a")] = i + 1
        map2[char2 - ord("a")] = i + 1

    return True

    # return len(set(s)) == len(set(t))


a = str("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJLMNPQRSTUVWXYZabc")
b = deepcopy(a) + "abcde"
print(b)
print(isIsomorphic(a, b))
print(len(a))
