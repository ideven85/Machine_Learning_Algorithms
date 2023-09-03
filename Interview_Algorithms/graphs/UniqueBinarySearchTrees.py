from math import factorial


class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return 1
        return factorial(n)//factorial(abs(n-2))

sol = Solution()
print([(i,sol.numTrees(i)) for i in range(1,20)])