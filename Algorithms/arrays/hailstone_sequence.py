def hailstone_sequence(n):
    if n == 1:
        return []

    return (
        [n // 2] + hailstone_sequence(n // 2)
        if n % 2 == 0
        else [n * 3 + 1] + hailstone_sequence(n * 3 + 1)
    )


def main():
    print(hailstone_sequence(10))


if __name__ == "__main__":
    main()
