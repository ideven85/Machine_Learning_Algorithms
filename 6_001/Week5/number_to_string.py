def number_to_string(n: int, b: int) -> str:
    digits = "0123456789"
    print(n, digits[n % b], end=" ")

    if n < 0:
        return number_to_string(-n, b)
    if n == 0:
        return "0"
    if n < b:
        return str(n)
    string_rep = "n"
    length = len(string_rep)

    print(n)
    return number_to_string(n // b, b) + digits[n % b]  # How on earth?


def myAtoi(s: str) -> int:
    #
    # if len(s) == 1 and not s.isdigit():
    #     return -myAtoi(s)
    if not s:
        return 0
    if len(s) == 1:
        return int(s[0])

    return int(s[-1]) + myAtoi(s[:-1]) * 10


#
print('\n', number_to_string(829, 11))
# print('\n',number_to_string(15,10))

print(myAtoi("829"))
# print(int("829"))
