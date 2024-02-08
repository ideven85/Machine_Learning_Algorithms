import math
from collections import defaultdict
from typing import List

"""
public static int minCount(int n) {
        if(n==0)
            return 0;
        int min=Integer.MAX_VALUE;
        for (int i = 1; i*i <=n ; i++) {
            int current=minCount(n-i*i);
            if(min>current)
                min=current;
        }
        return 1+min;

    }
"""

def numSquares( n: int) -> int:
   dp = [float('inf') for _ in range(n+1)]
   count = math.ceil(math.sqrt(n))
   dp[0]=0
   for i in range(1,n+1):
       dp[i]=float('inf')
       j=1
       while j<=count and j*j<=i:
            if i*i<j:
                break
            dp[i]=min(dp[i],dp[i-(j*j)]+1)
            j+=1
   return dp[n]



def minFallingPathSum( matrix: List[List[int]]) -> int:
    pass


print(numSquares(12))
print(numSquares(13))

print(numSquares(9999))




