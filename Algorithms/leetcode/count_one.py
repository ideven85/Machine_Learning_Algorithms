from typing import List


class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        Given an integer n, count the total number of digit 1 appearing in all non-negative integers
        less than or equal to n.
        """
        if n<=10:
            return n
        elif n<100:
            return n+1
        while 


        if n/1000==0:
            n/=1000



    def trailingZeroes(self, n: int) -> int:
        """
        Given an integer n, return the number of trailing zeroes in n!.
        """
        count = 0
        while n>0:
            n/=5
            count+=1
        return count

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            return [-1,-1]
        map = dict()

        for index,x in enumerate(nums):

            if target-x in map:
                return map[index,target-x]

            map[index]=x
        return [-1,-1]

