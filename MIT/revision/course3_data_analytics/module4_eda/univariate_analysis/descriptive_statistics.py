import numpy as np


def mid_range(lst):
    """Calculate Range and mid range

    Args:
        lst (list): list of numbers
    """
    x = np.array(lst)
    print(x.max() - x.min())
    print(np.median(x))


def mean_absolute_deviation(lst1, lst2):
    """Calculate mean absolute deviation

    Args:
        lst1 list): list of numbers
        lst2 list): list of numbers
    """
    x1, x2 = np.array(lst1), np.array(lst2)
    print(abs(np.average(x1) - np.average(x2)))


def main():
    mid_range([65, 81, 73, 85, 94, 79, 67, 83, 82])


if __name__ == "__main__":
    main()
