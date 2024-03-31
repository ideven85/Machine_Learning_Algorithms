def backspaceCompare(s: str, t: str) -> bool:
    stack = []
    stack2 = []
    for el in s:
        if stack and el == "#":
            stack.pop()

        elif el != "#":
            stack.append(el)
    for el in t:
        if stack2 and el == "#":
            stack2.pop()

        elif el != "#":
            stack2.append(el)
    # print(stack,stack2)
    return stack == stack2


s = "#ab##"
t = "c#d#"
print(backspaceCompare(s, t))
