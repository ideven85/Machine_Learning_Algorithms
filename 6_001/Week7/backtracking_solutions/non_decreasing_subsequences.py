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

    @cache
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


if __name__ == "__main__":
    nums = [2, 4, 7, 7]
    import time

    s1 = time.perf_counter()
    result = increasing_subsequences(nums)
    s2 = time.perf_counter()
    # print(result)
    x = non_decreasing_subsequences(nums)
    s3 = time.perf_counter()
    print(s2 - s1)

    print(s3 - s2)
    print(result)
    print(x)
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
