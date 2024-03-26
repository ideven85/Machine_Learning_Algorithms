def isPalindrome(s: str) -> bool:

    s = s.lower()
    inp = [x for x in s if 97 <= ord(x) <= 122]

    return not inp or not len(inp) == 1 and (len(inp) > 1 and inp == inp[::-1])


a = "0P"
print(isPalindrome(a))
