def uniquePaths(m: int, n: int) -> int:
    """
        There is a robot on an m x n grid.
        The robot is initially located at the top-left corner (i.e., grid[0][0]).
        The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
        The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot
    can take to reach the bottom-right corner.
    """
    if m * n == 0:
        return 0
    if m * n == 1:
        return 1
    grid = [[0 for _ in range(m)] for _ in range(n)]
    agenda = (0, 0)
