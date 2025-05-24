class Strings:

    def addStrings(self, num1: str, num2: str) -> str:

        n = len(num1)
        m = len(num2)
        carry = 0
        current = 0
        total = 0
        i = n - 1
        j = m - 1
        l = 0
        for l in range(min(n, m)):
            ch1 = num1[i]
            ch2 = num2[j]

            current = int(ch1) + int(ch2) + carry
            if current >= 10:
                carry = int(current // 10)
                current = current % 10

            i -= 1
            j -= 1

            total = total * 10 + current
        if i >= 0:
            current = int(num1[i]) + carry
            if current >= 10:
                carry = int(current // 10)
                current = current % 10

            total = total * 10 + current
            i -= 1
        if j >= 0:
            current = int(num2[j]) + carry
            if current >= 10:
                carry = int(current // 10)
                current = current % 10

            total = total * 10 + current
            j -= 1
        if carry != 0:
            total = total * 10 + carry
        total = str(total)
        return total[::-1]


def strStr(haystack: str, needle: str) -> int:
    pass


if __name__ == "__main__":
    a = Strings()
    s1 = "9"
    s2 = "9"
    print(a.addStrings(s1, s2))
