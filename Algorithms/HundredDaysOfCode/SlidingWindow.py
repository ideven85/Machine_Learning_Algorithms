from bisect import bisect_right
from collections import Counter
from typing import List


def longestNiceSubstring(s: str) -> str:
    longest = {}
    j=0;res=0
    count_characters = 0
    n = len(s)
    if n == 1:
        return ""
    for i in range(n-1):
        if s[i]==s[i+1] or abs(ord(s[i])-ord(s[i+1])==32):
            if s[i] not in longest or longest[s[i]]==0:
                longest[s[i]]=1
                count_characters+=1
        else:
            nice = False
            while not nice:
                if longest:
                    longest[s[j]]-=1
                    if longest[s[j]]==0:
                        if ord(s[j])>=97:
                            longest[(ord(s[j])-32)]=0
                        else:
                            longest[(ord(s[j])+32)]=0

                    j+=1
                else:
                    nice = True
                    
        res = max(res,i-j+1)
    return res


def threeSum(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        for i in range(n-2):
            if i == 0 or (i>0 and nums[i]!=nums[i-1]):
                ans = -nums[i]
                low = i+1
                high = n-1
                while low<high:
                    if nums[low]+nums[high]==ans:
                        answer.append([nums[i],nums[low],nums[high]])
                        print(answer,end=' ')
                        while nums[low]==nums[low+1] and low<n-2:
                            low+=1

                        while nums[high]==nums[high-1] and high>1:
                            high-=1

                        low+=1;high-=1
                    else:
                        if nums[low]+nums[high]>ans:
                            high-=1
                        else:
                            low+=1
        return answer


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        @cache
        def cached_bisect_right(val):
            nonlocal keys
            return bisect_right(keys, val)

        number_of = Counter(nums)
        keys = sorted(number_of)

        if number_of[0] >= 3:
            yield [0, 0, 0]
        if number_of[0] > 1:
            number_of[0] = 1
        for key in keys:

            # key_is_even
            if not key % 2:
                negative_key = -key // 2
                if number_of[negative_key] > 1:
                    yield [key, negative_key, negative_key]

        least = keys[0]
        if least > 0:
            return
        for i, key in enumerate(keys[:-1], 1):
            if key < 0:
                i = cached_bisect_right(-(key + key))
                no_positive_keys_for_that_key = i == len(keys)

                if no_positive_keys_for_that_key:
                    continue

            k = cached_bisect_right(-(least + key))

            for right in keys[i:k]:
                left = -(key + right)
                exist_left_that_negate_right_and_key = number_of[left]
                if exist_left_that_negate_right_and_key:
                    yield [left, key, right]

    # def threeSum(self, nums):
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums)-2):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         l, r = i+1, len(nums)-1
    #         while l < r:
    #             s = nums[i] + nums[l] + nums[r]
    #             if s < 0:
    #                 l += 1
    #             elif s > 0:
    #                 r -= 1
    #             else:
    #                 res.append([nums[i], nums[l], nums[r]])
    #                 while l < r and nums[l] == nums[l+1]:
    #                     l += 1
    #                 while l < r and nums[r] == nums[r-1]:
    #                     r -= 1
    #                 l += 1; r -= 1
    #     return res
