def isPalindrome(s: str) -> bool:

    s = s.lower()
    inp = [x for x in s if 97 <= ord(x) <= 122]

    return not inp or not len(inp) == 1 and (len(inp) > 1 and inp == inp[::-1])


a = "0P"
print(isPalindrome(a))


def combine(arr1, arr2):
    n = 3
    m = len(arr2) - 1
    first = 0
    second = 0
    total = n + m + 1
    while first <= n and second <= m:
        if arr1[first] < arr2[second]:
            arr1[total] = arr2[second]
            second += 1
        else:
            arr1[total] = arr1[first]
            first += 1
        total -= 1
        print(arr1)


a = [1, 4, 7, 20, 0, 0, 0]
b = [3, 4, 6]
combine(a, b)
print(a)
