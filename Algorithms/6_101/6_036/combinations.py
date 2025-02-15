def combinations(nums):
    """
    >>> combinations([5])
    {5}
    >>> combinations([1, 2])
    {0, 2, 3, -1}
    >>> combinations([2, 1])
    {1, 2, 3}
    >>> combinations([1, 2, 3])
    {0, 1, 2, 3, 5, 6, 9, -4, -3, -1}
    """
    if len(nums) < 2:
        return set(nums)
    return {op(old, nums[-1]) for old in combinations(nums[:-1]) for op in ops}


ops = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y,
]


def combinations_iterative(nums):
    if len(nums) < 2:
        return set(nums)
    out = set()
    for op in ops:
        out |= combinations_iterative([op(nums[0], nums[1])] + nums[2:])
    return out


def main():
    print(combinations([1, 2, 3]))

    print(combinations_iterative([1, 2, 3]))
    print(combinations([5]))
    print(combinations([1, 2, 3]))
    print(combinations([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
