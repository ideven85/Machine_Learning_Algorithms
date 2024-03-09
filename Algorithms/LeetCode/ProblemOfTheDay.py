from collections import Counter, defaultdict
from typing import List


def maxFrequencyElements(nums: List[int]) -> int:
    counter = Counter(nums)
    maxFreq = 0

    for value in counter.values():
        if maxFreq < value:
            maxFreq = value
    count = 0
    for value in counter.values():
        if value == maxFreq:
            count+=value
    #print(counter)

    d = defaultdict(int)
    for j in Counter(nums).values():
        d[j] += 1
    return max(d) * d[max(d)]
    #return count

print(maxFrequencyElements([1,2,3,4,5]))
