from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    if m * n == 0:
        return 0
    if m * n == 1:
        return grid[0][0]
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            dp[i][j] = grid[i][j]
            if i == 0 and j > 0:
                dp[i][j] += dp[i][j - 1]
            elif i > 0 and j == 0:
                dp[i][j] += dp[i - 1][j]
            else:
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid))
