import sys
from typing import List


def generatePermutations(array):

    def helper(array):
        if len(array) == 1:
            yield [array]

    for index, element in enumerate(array):
        remaining = array[:index] + array[index + 1 :]
        for permutations in helper(remaining):
            yield [element] + permutations
    return list(helper(array))


count = 0


def getPermutations1(array: List[int]) -> List[List[int]]:
    answer = []
    global count
    if len(array) == 1:
        count += 1
        return [array]
    for i in range(len(array)):
        for e in getPermutations1(array[:i] + array[i + 1 :]):
            answer.append([array[i]] + e)
    return answer


def powerset(array):
    subSets = [[]]
    for element in array:
        for i in range(len(subSets)):
            currentSubSet = subSets[i]
            subSets.append(currentSubSet + [element])
    return subSets


def subsequences(seq):
    if not seq:
        return []
    first = seq[0]
    rest = seq[1:]
    rest_seq = subsequences(rest)
    first_seq = [[first] + sub_seq for sub_seq in rest_seq]
    return first_seq + rest_seq


count = 0
sol = ""


def getPermutations(array, k):
    answer = []
    global count
    if len(array) == 1:
        count += 1

        return [array]
    for i in range(len(array)):
        for e in getPermutations(array[:i] + array[i + 1 :], k):

            answer.append([array[i]] + e)
    return answer


def getPermutation(n: int, k: int) -> str:
    a = list(range(1, n + 1))
    s = getPermutations(a, k)
    # print(s[k])
    # print(sol)
    answer = str()
    for e in s[k]:
        answer += str(e)
    return answer


def generatePermutationsV2(n):
    count = 1
    for i in range(1, n + 1):
        count *= i


def isArraySorted(arr):
    if len(arr) <= 1:
        return True

    return arr[0] <= arr[1] and isArraySorted(arr[1:])


def binaryStrings(n):
    if n == 0:
        return []
    if n == 1:
        return ["0", "1"]
    else:
        return [
            digit + bit for digit in binaryStrings(1) for bit in binaryStrings(n - 1)
        ]


def binaryKStrings(n, k):
    if n == 0:
        return []
    if n == 1:
        return [str(i) for i in range(k)]
    else:
        return [
            digit + bit
            for digit in binaryKStrings(1, k)
            for bit in binaryKStrings(n - 1, k)
        ]


def productSum(array, multiplier=1):
    # Write your code here.
    total = 0
    for e in array:
        if type(e) is list:
            total += productSum(e, multiplier + 1)
        else:
            total += e
    return total * multiplier


class PalindromePartitioning:

    answer = []

    def checkPalindrome(self, s, low, high):
        mid = low + (high - low) // 2
        for i in range(mid):
            if s[i] != s[high - i]:
                return False
        return True

    def generatePalindromes(self, s, low, temp):
        subSets = [[]]
        answer = []
        for element in s:
            for i in range(len(subSets)):

                currentSubSet = subSets[i]
                subSets.append(currentSubSet + [element])

            return subSets

    def partition(self, s) -> List[List[str]]:
        """
        Given a string s, find all possible permutations
        of s such that each permutation is a palindrome
        """
        subsets = [[]]
        s = list(s)
        for e in s:
            for i in range(len(subsets)):
                curr = subsets[i]
                print(curr + [e], end=" ")
                if len(curr + [e]) == 1:
                    subsets.append(curr + [e])
                elif curr + [e] == reversed(curr + [e]):
                    subsets.append(curr + [e])
        return subsets


class Solution:
    def dp(self, i, s, st):
        if i >= len(s):
            self.lst.append(list(st))
            return
        for j in range(i, len(s)):
            if s[i : j + 1] == "".join(reversed(s[i : j + 1])):
                st.append(s[i : j + 1])
                self.dp(j + 1, s, st)
                st.pop()
        return

    def partition(self, s: str) -> List[List[str]]:
        self.lst = []
        self.dp(0, s, [])
        return self.lst


class Solution2:
    def partition(self, s):
        result = []
        palindromes = [[] for _ in s]

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].append(s[l : r + 1])
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes[l].append(s[l : r + 1])
                l -= 1
                r += 1

        def backtrack(curr, i):
            if i == len(s):
                result.append(list(curr))
                return

            for el in palindromes[i]:
                curr.append(el)
                backtrack(curr, i + len(el))
                curr.pop()

        backtrack([], 0)
        return result


def fib(n):
    if n < 2:
        return n
    else:
        a = 0
        b = 1
        for i in range(1, n):
            b = a + b
            a = b - a
        return b


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 4]

    b = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

    print(getPermutation(3, 1))
    print(productSum(b))
    print(powerset(["1", "2", "3"]))
    s = ["n", "i", "t", "i", "n"]
    print("Palindrome Partitioning:")
    a1 = PalindromePartitioning().partition(s)
    print()
    print(a1)
    s = 3
    print(getPermutations1([]))
    print(getPermutations([1, 2, 1], 3))
    print("Binary K Strings:", binaryKStrings(5, 2))
    print("Subsequences", subsequences([1, 2, 3]))
