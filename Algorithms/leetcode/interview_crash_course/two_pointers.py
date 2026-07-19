def is_palindrome(s: str):
    """
    Example 1: Given a string s, return true if it is a palindrome, false otherwise.


    """

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

    # return True if list(s)==reversed(list(s)) else False


def main():
    a = "nitin"
    b = "sexya"
    print(f"{is_palindrome(a),is_palindrome(b)}")


if __name__ == "__main__":
    main()
