from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[0] = True
        jumps = nums[0]
        for i in range(1, n):
            for j in range(i, i + jumps):
                if j > n or nums[j - 1] == 0:
                    break
                elif dp[j - 1]:
                    dp[j] = True
            print(dp)
        return dp[n - 1]

    def canJump2(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, nums[i] + i)
        return True


sol = Solution()
nums = [0]

print(sol.canJump(nums))
