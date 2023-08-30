from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in duplicate:
                duplicate[nums[i]]=1
            else:
                return nums[i]
    def findDuplicateV2(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

def isHappy( n: int) -> bool:
    s = str(n)
    total = 0
    while True:

        if total==1:
            return True
        for e in s:
            total += int(e)*int(e)



print(isHappy(19))


a = Solution()
nums = [1,3,3,4,3]
print(a.findDuplicateV2(nums=nums))    
        