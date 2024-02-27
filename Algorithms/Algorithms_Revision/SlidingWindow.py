from collections import defaultdict
from typing import List


class Solution:
    """
    Given an array of integers, find the contiguous subarray (containing at least one)
    which has sum equal to s
    """


    def subArraySum(self, arr, n, s):
            curr = 0;
            left = 0
            for i in range(n):

                if arr[i] == s:
                    return [i + 1, i + 1]
                curr += arr[i]
                # print(curr,end=' ')
                if curr == s:
                    return [left + 1, i + 1]
                elif curr > s:
                    if left < i:
                        curr -= arr[left]
                        left += 1
                if curr == s:
                    return [left + 1, i + 1]
            while curr > s and left < n-1:
                curr -= arr[left]
                left += 1
            # print("HI")
            return [left + 1, n] if curr == s else [-1]
    def maxLen(self, n, X):
        H = defaultdict(int)
        subArraySum = 0
        maxLength = 0
        for i, x in enumerate(X):
            subArraySum = subArraySum + x
            if subArraySum == 0:
                maxLength = max(maxLength, i + 1)
            elif subArraySum not in H:
                H[subArraySum] = i
            else:
                maxLength = max(maxLength, i - H[subArraySum])
        return maxLength
def largestZeroSubarraySum(X: List[int]) -> int:
    H = defaultdict(int)
    subArraySum = 0
    maxLength = 0
    for i, x in enumerate(X):
        subArraySum = subArraySum + x
        if subArraySum == 0:
            maxLength = max(maxLength, i + 1)
        elif subArraySum not in H:
            H[subArraySum] = i
        else:
            maxLength = max(maxLength, i - H[subArraySum])
    return maxLength
a = [12,11,40,3];s=7
print(Solution().subArraySum(a,len(a),s))


