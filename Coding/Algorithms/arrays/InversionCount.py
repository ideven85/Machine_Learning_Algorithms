# arr[]: Input Array
# N : Size of the Array arr[]
# Function to count inversions in the array.
import time


def inversionCount(arr, n):
    def is_sorted(a):
        if len(a) <= 1:
            return True
        return a[0] <= a[1] and is_sorted(a[1:])

    count = 0
    flag = False
    n = len(arr)
    if n <= 1 or is_sorted(arr):

        return count
    element = arr[0]
    for i in range(1, n):
        if arr[i] > element:
            arr[0], arr[i] = arr[i], arr[0]
            inversionCount()


if __name__ == "__main__":
    arr = [1, 2, 3, 5, 4]
    n = len(arr)
    s = time.time()
    print(inversionCount(arr, n))
    print(time.time() - s)
