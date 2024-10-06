import time
from typing import List


def subsequences(s: List[int]):
    if not s:
        return {()}
    first = s[0]
    rest = s[1:]
    first_subsequence = subsequences(rest)
    rest_subsequence = {(first,) + sub_seq for sub_seq in subsequences(rest)}
    #  print("First:", first_subsequence)
    #  print("Rest:", rest_subsequence)
    return first_subsequence | rest_subsequence


def subsequences_v2(s: List[int]) -> List[List[int]]:
    sequences = [[]]
    for element in s:
        for i in range(len(sequences)):
            current_sequence = sequences[i]
            sequences.append(current_sequence + [element])
        # print(sequences)
    return sequences


def subsequences_alternative(seq):
    if not seq:
        return ""

    first = seq[0]
    rest = seq[1:]
    rest_subseq = subsequences_alternative(rest)
    result = ""
    for subseq in rest_subseq.split(" ", -1):

        result += " " + subseq
        result += " " + first + subseq

    return result[1:]


def string_subsequences(word):
    cache = {}

    def helper(w, partial):
        if not w:
            return partial

        # cache.setdefault()helper(w[1:],partial)+" "+helper(w[1:],w[0]+partial)
        return helper(w[1:], partial) + " " + helper(w[1:], partial + w[0])
        # return partial

    print(cache)
    return helper(word, "")


def main():
    # s1 = time.perf_counter_ns()
    # print(subsequences([1, 2, 3]))
    # e1 = time.perf_counter_ns()
    #
    #
    #
    # print(subsequences_v2([1, 2, 3]))
    # e2 = time.perf_counter_ns()
    print(string_subsequences("123"))
    e3 = time.perf_counter_ns()
    # l=string_subsequences("123")
    # print(list(l.split(",")))
    # print("First Approach", e1-s1)
    #
    # print("Second Approach:", e2 - e1)
    # print("For Strings:",e3-e2)


if __name__ == "__main__":
    main()
