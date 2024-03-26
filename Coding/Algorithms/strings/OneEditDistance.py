def isOneEditDistance(s: str, t: str) -> bool:
    n = len(s)
    m = len(t)
    if abs(n - m) > 2:
        return False
    dp = [[0 for _ in range(n)] for _ in range(n)]
