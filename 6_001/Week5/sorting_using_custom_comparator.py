import functools


def comparator(o1, o2):
    """
    Custom Comparator For Sorting Two Strings Lexicographically
    """
    if not o1 and not o2:
        return 0

    if len(o1) == len(o2):
        if o1[0] == o2[0]:
            return comparator(o1[1:], o2[1:])
        else:
            return ord(o1[0]) - ord(o2[0])
    else:
        return 1 if len(o1) > len(o2) else -1


shirts = [
    "orange",
    "oranges",
    "neat",
    "nike",
    "neal",
    "orange",
    "blue",
    "yellow",
    "",
    "",
    "yellow",
]
print(sorted(shirts, key=functools.cmp_to_key(comparator)))
