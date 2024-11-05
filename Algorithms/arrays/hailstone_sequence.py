def hailstone_sequence(n):
    if n == 1:
        return []

    return (
        [n // 2] + hailstone_sequence(n // 2)
        if n % 2 == 0
        else [n * 3 + 1] + hailstone_sequence(n * 3 + 1)
    )


def hailstone_sequence_alt(n, lst):
    if n == 1:
        return lst
    elif n // 2 == 0:
        lst.append(n // 2)
        return hailstone_sequence_alt(n // 2, lst)
    else:
        lst.append(n * 3 + 1)
        return hailstone_sequence_alt(n * 3 + 1, lst)


def main():
    print(hailstone_sequence(10))
    print(hailstone_sequence_alt(10, list()))


if __name__ == "__main__":
    main()
