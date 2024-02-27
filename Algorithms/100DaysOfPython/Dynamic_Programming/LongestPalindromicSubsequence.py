class LongestPalindromicSubsequence:

    def isPalindrome(self, s: str) -> bool:
        pass
    def longestPalindromeSubseq(self, s: str) -> int:



        """
        We are only interested in finding the maximum length of palindromic subsequence
        Brut Force Approach, We can use recursion to find the longest answer
        Then use hashmap to find the longest subsequence optimally
        Longest palindromic subsequence in between left and length of s
        """
        n = len(s)
        if n<=1:
            return n #Base Case

        pass



    #todo Doubt
    def longestIncreasingSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0]=1
        for i in range(1,n):
            for j in range(i+1,n):
                if s[j]>s[i] and dp[j]>dp[i]:
                    dp[i] = dp[j]
            dp[i]+=1
        return max(dp)




