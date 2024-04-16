"""
6.101 Recipes Optional Practice Exercise
Refactory - Recursion part 1
"""

# no imports allowed!

from debug_recursion import show_recursive_structure


@show_recursive_structure
def count_subparts(part_manifest: dict, part_num: int):
    """
        Recursively determine the number of total parts that will be needed to
        assemble the current part.
        pen_manifest = {
      5: [1, 2],
      3: [6, 5, 5, 5, 5],
      7: [1, 9],
      10: [3, 3, 3, 6]
    }
    where the corresponding part numbers to part names are:

        1 -> pen casing
        2 -> blue ink
        3 -> small pack of blue pens # Compound
        5 -> blue pen
        6 -> packaging
        7 -> black pen
        9 -> black ink
        10 -> large pack of blue pens
        Parameters:
            * part_manifest (dict<int, list<int>>) : a dictionary with integer part
                numbers mapping to a list of sub-part numbers needed to assemble the part.
                Each sub-part may or may not themselves be a key in the dictionary.
            * part_num (int) : the desired part to assemble.

        Returns:
            An integer representing the total number of subparts (including the
            number of subparts of any compound subparts.

        >>> x = {1: [2, 3, 2, 3], 3: [2, 4, 5], 4: [2, 7]}
        >>> count_subparts(x, 3)
        5
        >>> count_subparts(x, 2)
        0
        >>> count_subparts(x, 1)
        14
        >>> y = {5: [1, 2], 3: [6,5,5,5,5], 7: [1,9], 10: [3,3,3,6]}
        >>> count_subparts(y, 10)
        43
    """

    if part_num not in part_manifest:
        return 0
    else:

        current = part_manifest[part_num]
        total = len(current)
        for el in current:
            if el in part_manifest:
                total += count_subparts(part_manifest, el)
    return total


# todo
# @show_recursive_structure
def find_base_parts(part_manifest, part_num):
    """
    Recursively determine the unique base parts needed to assemble a part_num.

    Parameters:
        * part_manifest (dict<int, list<int>>) : a dictionary with integer part
            numbers mapping to a list of sub-part numbers needed to assemble the part.
            Each sub-part may or may not themselves be a key in the dictionary.
        * part_num (int) : the desired part to assemble.

    Returns:
        A set of integers representing the base parts needed to assemble the part.

    >>> x = {1: [2, 3, 2, 3, 6], 3: [2, 4, 5]}
    >>> list(sorted(find_base_parts(x, 3))) # returns a set {2, 4, 5}
    [2, 4, 5]
    >>> list(sorted(find_base_parts(x, 2))) # returns a set containing base part {2,}
    [2]
    >>> list(sorted(find_base_parts(x, 1))) # returns a set {2, 4, 5, 6}
    [2, 4, 5, 6]
    """
    out = list()
    if part_num not in part_manifest:
        if part_num not in out:
            out.append(part_num)
    else:
        for el in part_manifest[part_num]:
            if el in part_manifest:
                parts = part_manifest[el]
                # print(part_manifest)
                for x in parts:
                    if x not in out and x not in part_manifest:
                        out.append(x)

                find_base_parts(part_manifest, el)
            else:
                if el not in out:
                    out.append(el)
    return out


def maximum_steps(part_manifest):
    """
    Recursively determine the maximum number of assembly steps it would take to assemble
    a part in the manifest.

    Parameters:
        * part_manifest (dict<int, list<int>>) : a dictionary with integer part
            numbers mapping to a list of sub-part numbers needed to assemble the part.
            Each sub-part may or may not themselves be a key in the dictionary.

    Returns:
        An integer representing the maximum depth of the part_manifest.

    >>> maximum_steps({1: [2, 3, 2, 3], 3: [2, 4, 5]})
    2
    >>> maximum_steps({3: [2, 4, 5]})
    1
    >>> maximum_steps({2: [1], 4: [3, 2], 3: [2, 1]})
    3
    >>> maximum_steps({5: [1, 2], 3: [6,5,5,5,5], 7: [1,9], 10: [3,3,3,6]})
    3
    """

    def max_helper(part_num):
        """
        Given a part_num (int), return the maximum number of assembly steps.
        Base parts (parts that have no sub-parts) have 0 assembly steps.
        """
        if part_num not in part_manifest:
            return 0
        else:
            for el in part_manifest[part_num]:
                if el in part_manifest:
                    return 1 + max_helper(el)

        return 0

    max_depth = 0
    visited = set()
    for el in part_manifest.keys():
        current = 0
        if el in part_manifest:

            max_depth = max(max_helper(el), max_depth)

    return 1 + max_depth


if __name__ == "__main__":
    # Test with doctests. Helpful to debug individual practice.py functions.
    # import doctest
    #
    # _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    # doctest.testmod(optionflags=_doctest_flags, verbose=False)  # runs ALL doctests
    # # Alternatively, can run the doctests JUST for specified function/methods,
    # # e.g., for count_subparts or any other function you might want.  To
    # # do so, comment out the above line, and uncomment the below line of code.
    # # This may be useful as you write/debug individual doctests or functions.
    # # Also, the verbose flag can be set to True to see all test results,
    # # including those that pass.
    # #
    # """
    # doctest.run_docstring_examples(
    #     count_subparts,
    #     globals(),
    #     optionflags=_doctest_flags,
    #     verbose=True
    # )
    # """
    # # Your code below:
    x = {1: [2, 3, 2, 3], 3: [2, 4, 5], 4: [2, 7]}
    y = {5: [1, 2], 3: [6, 5, 5, 5, 5], 7: [1, 9], 10: [3, 3, 3, 6]}
    pen_manifest = {5: [1, 2], 3: [6, 5, 5, 5, 5], 7: [1, 9], 10: [3, 3, 3, 6]}
    print(count_subparts(pen_manifest, 10))
    print(find_base_parts(pen_manifest, 10))
