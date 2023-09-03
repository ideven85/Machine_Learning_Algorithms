from cmath import log
from collections import deque, defaultdict
from functools import cache
from typing import List

class Problems:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_far = 0; max_sum =0
        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(len(nums)):
            
            max_ending_far+=nums[i]
            if max_sum <= max_ending_far:
                max_sum = max_ending_far
            if max_ending_far < 0:
                max_ending_far = 0
           
        return max_sum
   
    def maxProduct(self, nums: List[int]) -> int:
        """
    Given an integer array nums, find a subarray that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.


        """
        product = 1;product_so_far = 1;
        n = len(nums)
        if n == 1:
            return nums[0]
        flag = False;flag1 = False
        for i in range(n):
            if nums[i]==0:
                flag = True
            if nums[i]>0:
                flag1 = True
            product_so_far*=nums[i]
            if product <= product_so_far:
                product = product_so_far
            if product_so_far <0:
                product_so_far = 1

        if flag and not flag1:
            return 0        
        if flag1:
            return product
        return product

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]= 1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j-1],max(dp[i-1][j],dp[i][j-1]))
        return dp[n][m]


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

class WellFormed:
    def __init__(self):
        self.opening='('
        self.closing=')'




def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    answer = 0
    ways = 0
    temp = n
    way=0
    total=0
    denoms.sort(reverse=True)
    for _ in range(len(denoms)):
        for e in denoms:
            if ways<=e:
                way=temp%e
                ways+=temp//e
                print(ways,end=' ')
                temp=temp%e
                total += temp%e
                print(total)

                temp = temp // e

            if total >= n:
                print("Goo")

                answer+=1
                total=0
                temp = n
                ways = 0




    print()

    return answer



def deleteAndEarn( nums: List[int]) -> int:
    points = defaultdict(int)
    max_number = 0
    # Precompute how many points we gain from taking an element
    for num in nums:
        points[num] += num
        max_number = max(max_number, num)

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






def canJump( nums: List[int]) -> bool:
    jumpsArray= [0 for _ in range(len(nums))]
    n = len(nums)
    if n == 0:
        return False
    if n == 1 and nums[0]!=0:
        return True
    if nums[0]==0:
        return False
    # To maximize the sum of jumps so that number of jumps can be minimized
    jumps = 0
    for i in range(n):
           if i +nums[i]==n-1:
               return True

           for j in range(i,i+nums[i]):
                if j>=n:
                    break

                jumpsArray[j]=max(jumpsArray[j],j)
                if jumpsArray[j]>=n:
                    return True
    print(jumpsArray)
    for i in range(1,n-1):
        if jumpsArray[i]==0:
            return False

    return True


            

def maxSubsetSumNoAdjacent(array:List[int])->int:
    # Write your code here.
    total = 0
    n = len(array)
    if n == 0:
        return 0
    if n == 1:
        return array[0]
    """ dp = [0 for _ in range(n)]
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])
    for i in range(2, n):
        if array[i] + dp[i - 2] > dp[i - 2]:
            dp[i] = max(array[i] + dp[i - 2], dp[i - 1])
        print(dp)

    t1 = array[0]
    t2 = max(array[0],array[1])
    for i in range(2,n):
        if array[i]+t1>t1:
            if t1+array[i]>t2:
                t1 = t1+array[i]
            else:
                t1 = t2
    """
    previous=0;current=0
    for e in array:
        previous,current=current,max(current,previous+e)
        print(current,end=' ')
    return current



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Problems().maxSubArray(nums=nums))
    nums1 = [5,4,-1,7,8]
    print(Problems().maxSubArray(nums=nums1))
    nums2 = [-1,-2,1]
    print(Problems().maxSubArray(nums=nums2))
    dp = Problems()
    print(dp.maxProduct(nums=nums1))
    print(dp.maxProduct(nums=nums))
    print(dp.maxProduct(nums=nums2))
    nums3 = [-2,0,-11]
    print(dp.maxProduct(nums3))
    s = "())((())("

    p = Problems()
    a = "b"
    b = "a"
    print(p.longestCommonSubsequence(a,b))
    nums = [2, 3, -2, 4]
    arr = [75, 105, 120, 75, 90, 135,20,10,10,2000]
    print(maxSubsetSumNoAdjacent(arr))
    n = 11
    denoms=[1,5,10]
    print("Change",numberOfWaysToMakeChange(n,denoms))
    nums2 = [2,2,3,4,5,]
    print(deleteAndEarn(nums2))
    array = [10, 70, 20, 30, 50, 11, 30]
    nums4 = [2, 3, 1, 1, 4]
    print(canJump(nums4))
    nums5 = [2, 0,0]
    print(canJump(nums5))