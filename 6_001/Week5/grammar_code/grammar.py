"""
Question 1: Fill in the expected value for all_phrases(grammar, "greeting")

Question 2: What are the base cases for all_phrases? The recursive cases?

Question 3: Implement all_phrases as defined below. You may test this function
by running `pytest test.py -v -x` (no quotes)
"""

from debug_recursion import show_recursive_structure


# @show_recursive_structure
def all_phrases(grammar, root):
    """
    Using rule lists in the grammar dict, expand root into all possible phrases.
    Each phrase is a tuple of terminal word strings.
    Return a set of all valid phrases.
    """
    pass


if __name__ == "__main__":
    # some small example test cases
    grammar = {
        "question": [["sentence", "?"]],
        "sentence": [["noun", "verb"], ["noun", "never", "verb"]],
        "noun": [["pigs"], ["professors"]],
        "verb": [["fly"], ["think"]],
        "greeting": [["hi", "noun"]],
    }

    # example
    expected = {("pigs",)}
    result = all_phrases(grammar, "pigs")
    assert result == expected, f"Got {result=} but {expected=}"

    # Q1
    expected = "TODO -- Insert expected result here"
    result = all_phrases(grammar, "greeting")
    assert result == expected, f"Got {result=} but {expected=}"

    expected = {
        ("pigs", "fly"),
        ("pigs", "think"),
        ("professors", "fly"),
        ("professors", "think"),
        ("pigs", "never", "fly"),
        ("pigs", "never", "think"),
        ("professors", "never", "fly"),
        ("professors", "never", "think"),
    }
    result = all_phrases(grammar, "sentence")
    assert result == expected, f"Got {result=} but {expected=}"

    expected = {
        ("pigs", "fly", "?"),
        ("pigs", "think", "?"),
        ("professors", "fly", "?"),
        ("professors", "think", "?"),
        ("pigs", "never", "fly", "?"),
        ("pigs", "never", "think", "?"),
        ("professors", "never", "fly", "?"),
        ("professors", "never", "think", "?"),
    }
    result = all_phrases(grammar, "question")
    assert result == expected, f"Got {result=} but {expected=}"