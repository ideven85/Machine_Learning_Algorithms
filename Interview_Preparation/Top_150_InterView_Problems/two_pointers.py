def isPalindrome( s: str) -> bool:

    # def isPalindrome_helper(inp:str,first:int,last:int) -> bool:
    #
    #
    #     if first == last:
    #         return True
    #     return inp[first] == inp[last-1] and isPalindrome_helper(inp,first+1,last-1)

    s=s.lower()
    inp = ""
    for char in s:
        if chr(97) <= char <= chr(122):
            inp+=char

    if not inp:
        return True
    if len(inp)==1:
        return False
    return inp == inp[::-1]


a = "nitin0123"
print(isPalindrome(a))

