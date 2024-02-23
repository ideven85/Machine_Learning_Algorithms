from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        matrix = []
        for i in range(n):
            matrix.append(triangle[i])
        
        dp = [[0 for _ in range(i)] for i in range(n)]
        dp[0][0]=matrix[0][0]
        for i in range(1,n):
            for j in range(len(matrix[i])):
                if matrix[i][j]<matrix[i+1][j] and dp[i-1][j]+
        
                
                