from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1, -1]
        mapping = dict()
        for index, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], index]
            mapping[num] = index
        print(mapping)
        return [-1, -1]


def main():
    nums = [2, 7, 11, 15]
    target = 22
    nums1 = [3, 3]
    target1 = 6
    sol = Solution()
    print(sol.twoSum(nums, target))
    print(sol.twoSum(nums1, target1))


if __name__ == "__main__":
    main()
