from typing import List

#todo
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        if n == 0:
            return 0
        lst = list(range(1, n + 1))  # O(n)
        n = len(nums)
        current_sum = sum(nums)  # O(n)
