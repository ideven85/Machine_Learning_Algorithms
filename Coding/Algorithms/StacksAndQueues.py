from collections import deque
import queue


class MyQueue:

    def __init__(self):
        self.front = []
        self.rear = []

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        if len(self.front) == 1:
            return self.front.pop()
        else:
            while len(self.front) > 1:
                self.rear.append(self.front.pop())
            return self.front.pop()

    def peek(self) -> int:
        if len(self.front) == 1:
            return self.front[len(self.front) - 1]
        else:
            return self.rear[len(self.rear) - 1]

    def empty(self) -> bool:
        return len(self.front) < 1


def longestValidParentheses(s: str) -> int:
    stack = deque()
    current = 0
    maxValid = 0
    for e in s:
        if e == "(":
            stack.append("(")
        elif e == ")":
            if stack:
                ch = stack.pop()
                if ch == "(":
                    current += 2
                    if maxValid <= current:
                        maxValid = current

                else:
                    stack.append("(")
            else:
                current = 0
    return maxValid


def myQueue():
    c = queue.Queue()
    c.put("first", block=True, timeout=0.5)
    c.put("second")
    print(c.get())
    print(c.get())
    print(c.empty())

    print(c.get(timeout=1))
    a = deque()
    a.append(1)
    a.append(2)
    print(a.pop())
    print(a.pop())
    print(a.pop())


def balancedBrackets(string):
    # Write your code here.
    stack = []
    balanced = False
    top = None
    for e in string:
        symbols = ["(", "[", "{"]
        closing = [")", "]", "}"]
        if e in symbols:
            stack.append(e)
        else:
            if len(stack) == 0:
                balanced = False
            elif e in closing:
                top = stack.pop()
                if not matches(top, e):
                    return False
                else:
                    balanced = True
    return balanced and len(stack) == 0


def matches(first, second):
    return (
        (first == "(" and second == ")")
        or (first == "[" and second == "]")
        or (first == "{" and second == "}")
    )


def longestBalancedBrackets(s):
    n = len(s)
    stack = []
    count = 0
    total = 0
    balanced = True
    for e in s:
        if e == "(":
            stack.append("(")
        else:
            if len(stack) == 0:

                balanced = False

            else:
                top = stack.pop()
                if top == "(":
                    count += 2
                    balanced = True
            if total < count:
                total = count
            if not balanced:
                count = 0
    return total


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = r = c = 0
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                c = max(c, l + r)
            elif l < r:
                l = r = 0
        l = r = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                c = max(c, l + r)
            elif l > r:
                l = r = 0
        return c


def nextGreaterElement(array):
    # Write your code here.
    stack = []
    n = len(array)

    return []


if __name__ == "__main__":

    s = "(a)"
    print(balancedBrackets(s))
    s1 = ")()()()(((((((()))"
    print(longestValidParentheses(s1))
    print(longestBalancedBrackets(s1))
    sol = Solution()
    print(sol.longestValidParentheses(s1))
