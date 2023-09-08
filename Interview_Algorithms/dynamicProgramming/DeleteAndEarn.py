from collections import defaultdict
from functools import cache
from math import log
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        two_back = one_back = 0
        n = len(points)
        if max_number < n + n * log(n, 2):
            one_back = points[1]
            for num in range(2, max_number + 1):
                two_back, one_back = one_back, max(one_back, two_back + points[num])
        else:
            elements = sorted(points.keys())
            one_back = points[elements[0]]
            for i in range(1, len(elements)):
                current_element = elements[i]
                if current_element == elements[i - 1] + 1:
                    two_back, one_back = one_back, max(one_back, two_back + points[current_element])
                else:
                    two_back, one_back = one_back, one_back + points[current_element]

        return one_back

def deleteAndEarn( nums: List[int]) -> int:
    points = defaultdict(int)
    max_number = 0
    # Precompute how many points we gain from taking an element
    for num in nums:
        points[num] += num
        max_number = max(max_number, num)
    print(points)
    print(max_number)
    @cache
    def max_points(num):
        # Check for base cases
        if num == 0:
            return 0
        if num == 1:
            return points[1]

        # Apply recurrence relation
        return max(max_points(num - 1), max_points(num - 2) + points[num])

    return max_points(max_number)

if __name__ == '__main__':
    nums = [3, 4, 2]
    sol=Solution()
    print(sol.deleteAndEarn(nums))
    print(deleteAndEarn(nums))