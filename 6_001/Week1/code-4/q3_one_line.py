"""
Try rewriting all of the provided examples using a single line
of code
"""

movies = ["Alien", "Barbie", "Clue", "Frozen", "Inception"]
ratings = [7.3, 8.5, 7.2, 7.4, 8.5, 3.3, 1.5]


def total_squares(n):
    return sum([i**2 for i in range(n)])


def average(numbers):
    return sum(numbers) / len(numbers)


def get_sample(samples, t):
    return samples[t] if 0 <= t < len(samples) else samples[0] if t < 0 else samples[-1]


def best_movie(movies, ratings):
    return [movie for movie, rating in zip(movies, ratings) if rating == max(ratings)][
        0
    ]


def nonnegative(numbers):
    """
    Given a list of numbers,
    return True if and only if all the numbers are nonnegative
    """

    return len([x for x in numbers if x < 0]) == 0


def nondecreasing(numbers):
    """
    Given a list of numbers,
    return True if and only if the numbers are in nondecreasing order
    """
    return sorted(numbers)==numbers


def above_threshold(numbers, thresh_val):
    """
    Given a list of numbers,
    return True if and only if at least one of the numbers is >= thresh_val
    """

    return len([x for x in numbers if x >= thresh_val]) >= 1


def check(result, expected):
    if isinstance(expected, float):
        assert abs(result - expected) <= 1e-6, f"got {result=} but {expected=}"
    else:
        assert result == expected, f"got {result=} but {expected=}"


if __name__ == "__main__":
    check(total_squares(20), 2470)
    s = [1, 2, 3, 4, 5]
    check(average(s), 3)
    check(get_sample(s, -3), 1)
    check(get_sample(s, 2), 3)
    check(get_sample(s, 10), 5)
    assert best_movie(movies, ratings) in {
        "Barbie",
        "Inception",
    }, f"Got best movie {best_movie(movies, ratings)}"
    check(nonnegative(s), True)
    check(nonnegative(s + [-1, 0]), False)
    check(nondecreasing(s), True)
    check(nondecreasing([1, 1, 2, 2, 3, 3]), True)
    check(nondecreasing([1, 1, 2, 1.99999]), False)
    check(above_threshold(s, 6), False)
    check(above_threshold(s, 4), True)
    check(above_threshold(s, 5), True)
    print("all correct!")
