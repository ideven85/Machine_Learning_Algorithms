from collections import Counter


def numJewelsInStones(jewels: str, stones: str) -> int:
    c = Counter(jewels)
    count = 0
    for el in stones:
        if el in c:
            count += c[el]
    return count


jewels = "z"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
