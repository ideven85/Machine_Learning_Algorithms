class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(','[','{']
        closing = [')',']','}']
        stack = [];balanced = False
        for element in s:
            if element in opening:
                stack.append(element)
            else:
                if len(stack) == 0:
                    return False
                elif element in closing:
                    top = stack.pop()
                    if not self.matches(top,element):
                        return False
                    else:
                        balanced = True
        return balanced and len(stack) == 0


    def matches(self,opening,closing):
        return (opening=='(' and closing == ')') or (opening == '[' and closing == ']') or (opening == '{' and closing == '}')

if __name__ == '__main__':
    balanced = Solution()
    s = "()[((({})))]({}"
    print(balanced.isValid(s))
