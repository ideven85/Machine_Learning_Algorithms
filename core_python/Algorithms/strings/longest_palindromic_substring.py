class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mapping = dict()
        first = 0
        last = n - 1
