from typing import List


def reverseStr(s: str, k: int) -> str:
    n = len(s)
    l = str()
    i = 0
    for i in range(0, n - 2 * k, 2 * k):
        for j in range(i + k - 1, i - 1, -1):
            l += s[j]
        if i + 2 * k < n:
            for j in range(i + k - 1, i + 2 * k):
                l += s[j]

    for i in range(n - 1, n - 2 * k, -1):
        l += s[i]
    s = str(l)
    return s


def lengthOfLongestSubstring(s: str) -> int:
    left = max_length = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def lengthOfLongestSubstringV2(s: str) -> int:

    subst = ""
    max_subst = 0
    for i in s:
        if i not in subst:
            subst += i
        else:
            ind = subst.index(i) + 1
            subst = subst[ind:] + i

        if len(subst) > max_subst:
            max_subst = len(subst)
    return max_subst


def addStrings(num1: str, num2: str) -> str:
    n = len(num1)
    m = len(num2)
    carry = 0
    current = 0
    total = 0
    i = n - 1
    j = m - 1
    l = 0
    for l in range(min(n, m)):
        ch1 = num1[i]
        ch2 = num2[j]

        current = int(ch1) + int(ch2) + carry
        carry = int(current // 10)
        i -= 1
        j -= 1

        total = total * 10 + current % 10
        print(total)
    if i > 0:
        total = total * 10 + int(num1[i])
        i -= 1
    if j > 0:
        total = total * 10 + int(num2[j])
        j -= 1

    return str(total)


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    longest = {}
    i = 0
    j = 0
    n = len(s)
    if k == 0:
        return 0
    if n == 1:
        return 1

    num_of_distinct = 0
    res = 0
    for i in range(n):
        if s[i] not in longest or longest[s[i]] == 0:
            num_of_distinct += 1
            longest[s[i]] = 1
        else:
            longest[s[i]] += 1
        while num_of_distinct > k:
            longest[s[j]] -= 1

            if longest[s[j]] == 0:
                num_of_distinct -= 1
            j += 1
        print(longest, end=" ")
        res = max(res, (i - j + 1))
    print(longest)
    return res


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    distinct = {}
    j = 0
    num_of_distinct = 1
    if k == 0:
        return True
    if len(nums) == 1 and k >= 1:
        return True

    k = k + 1

    for i in range(len(nums)):
        if nums[i] not in distinct or distinct[nums[i]] == 0:
            distinct[nums[i]] = 1
            num_of_distinct += 1
        else:
            distinct[nums[i]] += 1
            if distinct[nums[i]] > 1 and num_of_distinct <= k:
                return True
        while num_of_distinct > k:

            distinct[nums[j]] -= 1
            if distinct[nums[j]] == 0:
                num_of_distinct -= 1

            j += 1
        print(distinct, end=" ")
    return False


print(reverseStr("ABCDEFGHIJ", 3))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
s = "aba"
k = 1
print(lengthOfLongestSubstringKDistinct(s, k))
print(containsNearbyDuplicate([1, 2, 3, 1], 2))
print(addStrings("123", "11"))
print(lengthOfLongestSubstring("aabaab!bb"))
