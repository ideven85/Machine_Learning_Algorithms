import functools
from typing import List


class LargestNumber:
    def printLargest(self, arr:List[str]) -> str:
        def compare(num1, num2):

            if (num1+num2)>(num2+num1):
                return -1
            elif (num1+num2)<(num2+num1):
                return 1
            else:
                return 0
        n = len(arr)
        if n == 0:
            return ""
        arr.sort(key=functools.cmp_to_key(compare))
        return ''.join(arr)



l = LargestNumber()

print(l.printLargest(["54", "546", "548", "60"]))