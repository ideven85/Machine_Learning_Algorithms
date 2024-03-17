import doctest
from collections import defaultdict
from typing import List


# Map<Integer,Integer> map = new HashMap<>();
# total+=nums[i-1];
# if(map.containsKey(goal-total)) count+=1;
# left+=1; total-=nums[left];
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    """
    Parameters:
    @param nums: A binary array nums
    @param goal: An integer goal,
    @return:  The number of non-empty subarrays with a sum goal.
    >>>numSubarraysWithSum(nums=[1,0,1,0,1],goal=2)
    4
    """
    mapping = defaultdict(int)
    n = len(nums)
    if n==1:
        if nums[0]==goal:
            return 1
        else:
            return 0
    count = 0
    total = 0
    left = 0
    right = 0
    for i in range(n):
        if not nums[i]:
            continue
        total += nums[i]
        if mapping[goal-total]:
            count+=1
            total -=nums[left]
            left+=1

        mapping[total]=i
        if total > goal:
            while total > goal:
                total -=nums[left]
                left+=1



def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, return an array answer such that
    answer[i] is equal to the product of all the elements of nums except nums[i].
    >>> productExceptSelf([1,2,3,4])
    [24,12,8,6]
    """
    answer = [0 for _ in range(len(nums))]
    answer[0]=1
    n = len(nums)
    for i in range(1, len(nums)):
        answer[i] = answer[i-1]*nums[i-1]
    right = 1
    for i in range(n-1,-1,-1):
        answer[i]*=right
        right *= nums[i]

    return answer


if __name__ == '__main__':

    n = 4
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        print(n)
    print(productExceptSelf([1,2,3,4]))