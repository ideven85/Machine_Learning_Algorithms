from typing import List


def minCostClimbingStairs( cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        dp = [0 for _ in range(n)]
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i]=min(dp[i-2]+cost[i],dp[i-1]+cost[i])
        return min(dp[n-1],dp[n-2])


if __name__ == '__main__':
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))


