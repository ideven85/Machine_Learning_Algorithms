from typing import List


def lis(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]

    dp[0]=1
    for i in range(1,n):
        for j in range(n):
            if nums[j]<nums[i] and dp[j]>dp[i]:
                dp[i]=dp[j]
        dp[i]+=1
        print(dp)
    print(dp)
    return max(dp)


#todo
def findNumberOfLIS( nums: List[int]) -> int:
    pass




if __name__ == '__main__':
    nums = [90,93,94,95,99,1,2,3,97,98,101,102,103,107,111,112,113,114]
    nums1 = [1, 3, 5, 4, 7]
    print(lis(nums))