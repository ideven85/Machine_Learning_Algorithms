from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    first = m - 1
    second = n - 1
    total = first + second + 1
    while second >= 0:
        if first >= 0 and nums1[first] > nums2[second]:
            nums1[total] = nums1[first]
            first -= 1
        else:
            nums1[total] = nums2[second]
            second -= 1
        total -= 1
        # print(nums1)


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 4, 6]
    merge(a, 3, b, 3)
    print(a)
