def is_valid(s: str) -> bool:
    OPENING = ["(", "[", "{"]
    CLOSING = [")", "]", "}"]
    n = len(s)
    if n == 0:
        return True
    stack = []
    for el in s:
        if el in OPENING:
            stack.append(el)
        elif el in CLOSING:
            if not stack:
                return False
            closing_index = CLOSING.index(el)
            current = stack.pop()
            opening_index = OPENING.index(current)
            if opening_index != closing_index:
                return False
    # print(stack)
    return False if len(stack) != 0 else True


s = "(([](}))"
print(is_valid(s))
