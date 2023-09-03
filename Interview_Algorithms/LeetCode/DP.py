import time
from functools import cache
from typing import List


def fib(n):
    if n<2:
        return n
    else:
        if n in memo:
            return memo[n]
        memo[n]=fib(n-1)+fib(n-2)

memo = {}


def rob( nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    current=0;previous=0
    for e in nums:
        previous,current=current,max(current,previous+e)
    return current
def mostPoints( questions: List[List[int]]) -> int:
    # questions = [[3,2],[4,3],[4,4],[2,5]]

    @cache
    def dp(i):
        if i >=len(questions):
            return 0

        j = i+questions[i][1]+1
        print(i, j)
        return max(questions[i][0]+dp(j),dp(i+1))





    return dp(0)

def mostPointsBottomUp(questions: List[List[int]])->int:
    n = len(questions)
    dp = [0 for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        j = i+questions[i][1]+1
        dp[i]=max(questions[i][0]+dp[min(j,n)],dp[i+1])
    print(dp)
    return dp[0]
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) //( factorial(n - 1) * factorial(m - 1))

a = [fib(i) for i in range(10000)]
print(time.time())
print(a)
print(time.time())

houses = [2,7,9,3,1]
print(rob(houses))
questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
#questions.sort( key=lambda x: x[1])
#print(questions)
n = len(questions)

print(mostPoints(questions))
print(mostPointsBottomUp(questions))
sol = Solution()
print(sol.uniquePaths(3,7))