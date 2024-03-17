from typing import List


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n==0:
            return res
        def dfs(res,left,right,intermediate,n):
            if len(intermediate)==2*n:
                res.append(intermediate)
            if left<n:
                dfs(res,left+1,right,intermediate+"(",n)
            if left>right:
                dfs(res,left,right+1,intermediate+")",n)

        dfs(res,0,0,"",n)
        return res

if __name__ == '__main__':
    parenthesis = GenerateParenthesis()
    print(parenthesis.generateParenthesis(5))



