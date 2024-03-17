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



class LongestIncreasingSubsequence:

    # todo Doubt
    def longestIncreasingSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            for j in range(i + 1, n):
                if s[j] > s[i] and dp[j] > dp[i]:
                    dp[i] = dp[j]
            dp[i] += 1
        return max(dp)

class LongestPalindromicSubString:
    """
    Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

    """
    def longestPalindromicSubString(self,s: str) -> str:
        n = len(s)
        left = 0
        right  = 0
        for i in range(n):
            l1 = self._expandAroundCenter(s,i,i)
            l2 = self._expandAroundCenter(s,i,i+1)

            length = max(l1,l2)
            if length > (right - left):
                left,right = (i-(length-1)//2,i+length//2)
                print(left,right,length)


        return s[left:right+1] # Got No idea how this is working

    def _expandAroundCenter(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return right-left-1

    def longestPalindromicSubStringV2(self, s:str)->str:


        # Brut-Force Approach
        def check(i,j):
            LEFT = i
            RIGHT = j-1

            while LEFT<=RIGHT:
                if s[LEFT]!=s[RIGHT]:
                    return False
                LEFT+=1
                RIGHT-=1
            return True

        for right in range(len(s),0,-1):
            for left in range(len(s)-right+1):
                if check(left,left+right):
                    return s[left:left+right]
        return ""


print(LongestPalindromicSubString().longestPalindromicSubStringV2("babbd"))


