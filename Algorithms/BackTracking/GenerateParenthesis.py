from functools import cache, lru_cache
from typing import List


class GenerateParenthesis:
    def generateParenthesis(self, n: int):
        res = set()
        if n == 0:
            return res

        @lru_cache(maxsize=None)
        def dfs(left, right, intermediate):
            if len(intermediate) == 2 * n:
                res.add(intermediate)
            if left < n:
                dfs(left + 1, right, intermediate + "(")
            if left > right:
                dfs(left, right + 1, intermediate + ")")

        dfs(0, 0, "")
        return list(res)


if __name__ == "__main__":
    parenthesis = GenerateParenthesis()
    print(parenthesis.generateParenthesis(10))
