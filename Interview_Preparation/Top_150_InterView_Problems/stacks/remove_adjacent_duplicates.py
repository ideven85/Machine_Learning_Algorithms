import time
from collections import deque


def remove_duplicates(self, s: str) -> str:
    stack = deque()
    n = len(s)
    if n == 1:
        return s
    i = 0
    while i < n:
        if stack and stack[-1] == s[i]:
            # print(stack[-1])
            stack.pop()

        else:
            stack.append(s[i])
        i += 1
    return "".join(stack)


start = time.time() * 1_000_000
s = "azxxzy"
print(remove_duplicates(s))
end = time.time() * 1_000_000
print(end - start)
