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


# Question 4
def combos(inp):
    """
        Given a list of elements, write a function that returns a list of lists, consisting of all of the possible combinations
    of the elements of the original list. Elements in the original list can be assumed to be unique (i.e., appear in
    the list only once). Note that the order of the elements in each combination, and the order of combinations in
    the output list, do not matter.
    >>> sorted(combos([1, 2]))
    [[], [1], [1, 2], [2]]
    >>> sorted(combos([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    if not inp:
        return [[]]
    clist = []
    # for el in inp:
    #     for i in range(len(clist)):
    #         temp = clist[i]
    #         clist.append(temp+[el])
    # return clist
    for combo in combos(inp[1:]):
        clist.append(combo)
        clist.append(inp[0:1] + combo)
    return clist


# Question 4b:
def combos_gen(inp):
    """
        Given a list of elements, write a function that returns a list of lists, consisting of all of the possible combinations
    of the elements of the original list. Elements in the original list can be assumed to be unique (i.e., appear in
    the list only once). Note that the order of the elements in each combination, and the order of combinations in
    the output list, do not matter.
    >>> sorted(combos_gen([1, 2]))
    [[], [1], [1, 2], [2]]
    >>> sorted(combos_gen([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    """
    if not inp:
        yield []
        return
    for combinations in combos_gen(inp[1:]):
        yield inp[0:1] + combinations
        yield combinations


def main():
    s1 = time.perf_counter_ns()
    print("Old:", sorted(subsequences([1, 2])))
    e1 = time.perf_counter_ns()
    print("Old took", e1 - s1)
    s2 = time.perf_counter_ns()
    print("Generator:", sorted(combos_gen([1, 2])))
    e2 = time.perf_counter_ns()
    print("Generator took:", e2 - s2)
    s4 = time.perf_counter_ns()
    print("List new :", sorted(combos([1, 2])))
    e4 = time.perf_counter_ns()
    print("List new  took:", e4 - s4)
    #
    #
    #
    # print(subsequences_v2([1, 2, 3]))
    # e2 = time.perf_counter_ns()
    s = string_subsequences("123")
    print(s.split())
    e3 = time.perf_counter_ns()
    l = string_subsequences("123")
    print(list(l.split(",")))
    print("First Approach", e1 - s1)

    print("Second Approach:", e2 - e1)
    print("For Strings:", e3 - e2)


if __name__ == "__main__":
    main()
