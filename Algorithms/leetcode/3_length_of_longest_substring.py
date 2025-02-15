class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
                Given a string s, find the length of the longest
        substring
         without repeating characters.
        """
        if len(s) < 2:
            return len(s)

        left, curr, maximum = 0, 0, 0

        s1 = set()
        while curr < len(s):
            # print(s1)
            while s[curr] in s1:
                s1.remove(s[left])
                left += 1

            s1.add(s[curr])
            curr += 1
            maximum = max(maximum, curr - left)

        # print(maximum)

        return maximum


def main():
    s = "abcabcbb"
    s2 = "abcde"
    s3 = "aabaab!ab"
    sol = Solution()
    print(Solution().lengthOfLongestSubstring(s))
    print(sol.lengthOfLongestSubstring(s2))
    print(sol.lengthOfLongestSubstring(s3))
    # print(len("cvdeaghij"))


if __name__ == "__main__":
    main()
