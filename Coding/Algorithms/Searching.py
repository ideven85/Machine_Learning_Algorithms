from typing import List


def binarySearch(array, target):
    # Write your code here.
    n = len(array)
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == array[mid]:
            return mid
        if target < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def findThreeLargestNumbers(array: List[int]) -> List[int]:
    # Write your code here.
    answer = []
    min1 = -float("inf")
    for e in array:
        if min1 <= e:
            min1 = e
    answer.append(min1)
    array.remove(min1)
    min1 = -float("inf")
    for e in array:
        if min1 <= e:
            min1 = e
    array.remove(min1)
    answer.append(min1)
    min1 = -float("inf")
    for e in array:
        if min1 <= e:
            min1 = e

    answer.append(min1)
    answer.reverse()
    return answer


if __name__ == "__main__":
    a = list(range(1, 10))
    print(binarySearch(a, 22))
    arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    print(findThreeLargestNumbers(arr))
