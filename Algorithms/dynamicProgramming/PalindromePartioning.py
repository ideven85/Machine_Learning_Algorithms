from typing import List


class PalindromePartioning:
    def dp(self, i, s, st):
        if i >= len(s):
            self.lst.append(list(st))
            return
        for j in range(i, len(s)):
            if s[i : j + 1] == "".join(reversed(s[i : j + 1])):
                st.append(s[i : j + 1])
                self.dp(j + 1, s, st)
                st.pop()
        return

    def partition(self, s: str) -> List[List[str]]:
        self.lst = []
        self.dp(0, s, [])
        return self.lst

    def minCut(self, s: str) -> int:
        pass


from dis import dis

if __name__ == "__main__":
    s = "aab"
    x = PalindromePartioning().partition(s)
    dis(PalindromePartioning().partition)

    print(x)
