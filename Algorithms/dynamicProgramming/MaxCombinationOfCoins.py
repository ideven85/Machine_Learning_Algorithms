from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        toCompare=0
        dp[0]=1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    dp[j]+=dp[j-coins[i]]


        print(dp)
        return dp[amount]

sol = Solution()
amount = 5; coins = [1,2,5]
print(sol.change(amount,coins))