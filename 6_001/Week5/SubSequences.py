import time
from typing import List


def subsequences(s: List[int]):
    if not s:
        return {()}
    first = s[0]
    rest = s[1:]
    first_subsequence = subsequences(rest)
    rest_subsequence = {(first,) + sub_seq for sub_seq in subsequences(rest)}
    print("First:", first_subsequence)
    print("Rest:", rest_subsequence)
    return first_subsequence | rest_subsequence


start = time.time()
print(subsequences([1, 2, 3]))
end = time.time()
print("First Approach:", end - start)


def subsequencesV2(s: List[int]) -> List[List[int]]:
    sequences = [[]]
    for element in s:
        for i in range(len(sequences)):
            current_sequence = sequences[i]
            sequences.append(current_sequence + [element])
        # print(sequences)
    return sequences


start = time.time()
print(subsequencesV2([1, 2, 3]))
end = time.time()
print("Second Approach:", end - start)
