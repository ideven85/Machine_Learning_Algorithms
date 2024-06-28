from collections import deque
from functools import lru_cache, cache
import sys

sys.setrecursionlimit(100000)


def increasing_subsequences(arr):

    # @lru_cache(maxsize=None)
    memo = set()

    # @cache
    def dfs(last, current=None, start=0):

        if current is None:
            current = list()
        if len(current) >= 2:
            # print(current,end=' ')
            if current not in output:
                output.append(current[:])

            # count[0]+=1

        for i in range(start, last):
            # print(i,end=' ')

            if not current or arr[i] >= current[-1]:
                # print(current)
                # current.add(f)
                current.append(arr[i])
                dfs(last, current, i + 1)
                current.pop()

    output = []
    # count=[0]
    dfs(len(arr))

    return output


def non_decreasing_subsequences(nums):

    n = len(nums)

    @lru_cache(maxsize=None)
    def recurse(start):
        num = nums[start]
        memo = set()
        sol = [[num]]
        for i in range(start + 1, n):
            next_num = nums[i]
            if next_num not in memo and next_num >= nums[i]:
                memo.add(next_num)
                sol.extend(([num] + s) for s in recurse(i))
        return sol

    memo = set()
    out = []
    for start in range(n):
        if nums[start] not in memo:
            memo.add(nums[start])
            out.extend(s for s in recurse(start) if len(s) >= 2)

    return out

def lis( nums):
    """
    @param nums: List of integers
    @return length of longest increasing subsequence
    """
    n = len(nums)
    memo = {n-1:1}

    @cache
    def dfs(i):
        if i in memo:
            return memo[i]
        res = 1

        for j in range(i+1,n):
            if nums[j]>nums[i]:
                res = max(res,1+dfs(j))
        memo[i]=res
        return memo[i]
    out = [dfs(i) for i in range(n)]
    print(memo)
    return max(out)

def longest_subsequence(nums):
    n = len(nums)
    dp = [0 for _ in range(n+1)]
    dp[0]=1
    # for i in range(1,n):
    #     for j in range(n):
    #         if nums[i]>nums[j] and dp[j]>dp[i]:
    #             dp[i]=dp[j]
    #     dp[i]+=1
    #     print(dp)
    for i in range(1,n):
        dp[i]=1
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[i],1+dp[j])
        print(dp)
    return max(dp)



if __name__ == "__main__":
    nums = [2,4,3,8]
    import time

    s1 = time.perf_counter()
    #result = increasing_subsequences(nums)
    s2 = time.perf_counter()
    # print(result)
    x = non_decreasing_subsequences(nums)
    s3 = time.perf_counter()
    print(s2 - s1)

    print(s3 - s2)
    print(lis(nums))
    print(longest_subsequence(nums))
    #print(result)
    #print(x)
#
# if __name__ == "__main__":
#     inp = [2, 4, 5, 4]
#     print(increasing_subsequences(inp))
#
#
# """
# Input: [2, 4, 5, 4]
# Output: [[2, 4, 5], [2, 5], [2, 4], [4, 5]]
# """
