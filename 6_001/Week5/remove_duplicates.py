def remove_duplicates(arr):
    if not arr or len(arr) == 1:
        return
    n = len(arr)
    i = n - 1
    last = n - 1
    k = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[k] = arr[i]
            k += 1

    return k


a = [1, 1, 2, 2, 2, 3]
print(remove_duplicates(a))
print(a)
