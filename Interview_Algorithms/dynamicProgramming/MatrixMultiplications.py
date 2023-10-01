from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @lru_cache(2000)

        def dp(i:int,left:int)->int:
            if i==m:
                return 0
            multiplier = multipliers[i]
            right=n-1-(i-left)
            if cacheMap[i][left]!=0:
                return cacheMap[i][left]
            cacheMap[i][left]=max(multiplier*nums[left]+dp(i+1,left+1),multiplier*nums[right]+dp(i+1,left))
            return cacheMap[i][left]



        n = len(nums)
        m = len(multipliers)
        cacheMap = [[0 for _ in range(m+1)] for _ in range(m+1)]
        return dp(0,0)

nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]
s = Solution()
print(s.maximumScore(nums,multipliers))


