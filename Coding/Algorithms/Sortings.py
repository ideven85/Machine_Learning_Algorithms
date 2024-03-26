def insertionSort(array):
    # Write your code here.
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def subarraySort(array):
    # Write your code here.

    """index=-1;index2=-1
    curr_index = 0
    for high in range(n-1,0,-1):
        if array[high]<array[high-1]:
            curr_index=high
            index = curr_index+1
            break
    print(curr_index)
    if curr_index<=0:
        return [-1,-1]
    for i in range(curr_index-1,0,-1):
        if array[i]>=array[curr_index]:
            index2=i


    print(array[index],array[index2])
    return [index2,index]
    """
    n = len(array)
    low = 0
    high = n - 1
    index1 = -1
    index2 = -1
    curr_length = 0
    while low < high:
        if low == high:
            return [-1, -1]

        if array[low] < array[low + 1] and array[low + 1] < array[high]:
            low += 1
        else:
            index1 = low
        if array[high] > array[high - 1] and array[low] < array[high - 1]:
            high -= 1
        else:
            index2 = high
        if array[low] >= array[high]:
            index1 = low
            index2 = high
            curr_length = index2 - index1
            break
        low += 1
        high -= 1
    return [index1, index2]


def subarraySortV2(array):
    low = float("inf")
    high = -float("inf")
    for i in range(len(array)):
        if isNotSorted(array, array[i], i):
            low = min(low, array[i])
            high = max(high, array[i])
    if low == float("inf"):
        return [-1, -1]
    index1 = 0
    print(low, high)
    while low >= array[index1]:
        index1 += 1
    index2 = len(array) - 1
    while high <= array[index2]:
        index2 -= 1
    return [index1, index2]


def isNotSorted(array, num, index):
    if index == 0:
        return num > array[index + 1]
    if index == len(array) - 1:
        return num < array[index - 1]
    return num > array[index + 1] or num < array[index - 1]


if __name__ == "__main__":
    a = [
        1,
        2,
        3,
        4,
        5,
        6,
        18,
        21,
        22,
        7,
        14,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        19,
        4,
        14,
        11,
        6,
        33,
        35,
        41,
        55,
    ]
    # a = insertionSort(a)
    b = [1, 2, 5, 3, 4]
    print(subarraySortV2(a))
    print(subarraySortV2(list(range(1, 10))))
    print(subarraySortV2(b))
