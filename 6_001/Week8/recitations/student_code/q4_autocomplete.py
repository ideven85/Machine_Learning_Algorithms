"""
Question 4: Look at the correct implementation of autocomplete provided below.
How could we refactor this code to increase efficiency?

Note: you will have to copy / paste your lab into lab.py!
"""

from lab import PrefixTree, word_frequencies
from test import read_expected


def autocomplete(ptree, prefix, max_count=None):
    if not isinstance(prefix, str):
        raise TypeError

    all_words = [i for i in ptree if i[0].startswith(prefix)]

    if max_count is None:
        max_count = len(all_words)

    out_words = []
    for _ in range(max_count):
        best = (None, float("-inf"))
        for i in all_words:
            if i[1] > best[1] and i not in out_words:
                best = i
        if best != (None, float("-inf")):
            out_words.append(best)

    return [i[0] for i in out_words]


def test_autocomplete_small():
    # Autocomplete on simple prefix trees with less than N valid words
    t = word_frequencies("cat car carpet")
    result = autocomplete(t, "car", 3)
    assert set(result) == {"car", "carpet"}

    t = word_frequencies("a an ant anteater a an ant a")
    result = autocomplete(t, "a", 2)
    assert set(result) in [{"a", "an"}, {"a", "ant"}]

    t = word_frequencies("man mat mattress map me met a man a a a map man met")
    result = autocomplete(t, "m", 3)
    assert set(result) == {"man", "map", "met"}

    t = word_frequencies("hello hell history")
    result = autocomplete(t, "help", 3)
    assert result == []


def test_autocomplete_big_1():
    alphabet = a = "abcdefghijklmnopqrstuvwxyz"

    word_list = [
        "aa" + l1 + l2 + l3 + l4 for l1 in a for l2 in a for l3 in a for l4 in a
    ]
    word_list.extend(["apple", "application", "apple", "apricot", "apricot", "apple"])
    word_list.append("bruteforceisbad")

    t = word_frequencies(" ".join(word_list))
    for i in range(50_000):
        result1 = autocomplete(t, "ap", 1)
        result2 = autocomplete(t, "ap", 2)
        result3 = autocomplete(t, "ap", 3)
        result4 = autocomplete(t, "ap")
        result5 = autocomplete(t, "b")

        assert set(result1) == {"apple"}
        assert set(result2) == {"apple", "apricot"}
        assert set(result4) == set(result3) == {"apple", "apricot", "application"}
        assert set(result5) == {"bruteforceisbad"}


def test_autocomplete_big_2():
    nums = {
        "t": [0, 1, 25, None],
        "th": [0, 1, 21, None],
        "the": [0, 5, 21, None],
        "thes": [0, 1, 21, None],
    }
    with open("testing_data/frankenstein.txt", encoding="utf-8") as f:
        text = f.read()
    w = word_frequencies(text)
    for i in sorted(nums):
        for n in nums[i]:
            result = autocomplete(w, i, n)
            expected = read_expected("frank_autocomplete_%s_%s.pickle" % (i, n))
            assert len(expected) == len(result), (
                ("missing" if len(result) < len(expected) else "too many")
                + " autocomplete results for "
                + repr(i)
                + " with maxcount = "
                + str(n)
            )
            assert set(expected) == set(result), (
                "autocomplete included "
                + repr(set(result) - set(expected))
                + " instead of "
                + repr(set(expected) - set(result))
                + " for "
                + repr(i)
                + " with maxcount = "
                + str(n)
            )


def test_autocomplete_big_3():
    with open("testing_data/frankenstein.txt", encoding="utf-8") as f:
        text = f.read()
    w = word_frequencies(text)
    the_word = "accompany"
    for ix in range(len(the_word) + 1):
        test = the_word[:ix]
        result = autocomplete(w, test)
        expected = read_expected("frank_autocomplete_%s_%s.pickle" % (test, None))
        assert len(expected) == len(result), (
            ("missing" if len(result) < len(expected) else "too many")
            + " autocomplete results for "
            + repr(test)
            + " with maxcount = "
            + str(None)
        )
        assert set(expected) == set(result), (
            "autocomplete included "
            + repr(set(result) - set(expected))
            + " instead of "
            + repr(set(expected) - set(result))
            + " for "
            + repr(test)
            + " with maxcount = "
            + str(None)
        )


if __name__ == "__main__":
    import time

    for test in [
        test_autocomplete_small,
        test_autocomplete_big_1,
        test_autocomplete_big_2,
        test_autocomplete_big_3,
    ]:
        start = time.perf_counter()
        test()
        end = time.perf_counter()
        print(f"{test.__qualname__} took {end-start} seconds to complete")


## word_frequencies


def get_words(text):
    return [tuple(i.split()) for i in tokenize_sentences(text, True)]


def word_frequencies(text):
    words = PrefixTree()
    for sentence in get_words(text):
        for word in sentence:
            if word not in words:
                words[word] = 0
            words[word] += 1
    return words


# def word_frequencies(text):
#     words = PrefixTree()
#     for sentence in get_words(text):
#         for word in sentence:
#             increment(words, word)
#     return words

# def increment(ptree, value):
#     node = ptree._get_node(value, True)
#     if node.value is None:
#         node.value = 0
#     node.value += 1


## autocomplete


def autocomplete(ptree, prefix, max_count=None):
    if not isinstance(prefix, str):
        raise TypeError

    all_words = [i for i in ptree if i[0].startswith(prefix)]

    if max_count is None:
        return [i[0] for i in all_words]

    sorted_words = sorted(all_words, reverse=True, key=lambda x: x[1])
    return [i[0] for i in sorted_words[:max_count]]
