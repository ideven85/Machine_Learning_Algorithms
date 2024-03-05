from collections import defaultdict
from typing import List

class Problems:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            mapping[tuple(sorted(s))].append(s)
        sb = []
        for v in mapping.values():
            sb.append(list(v))
        return sb
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1=-1;index2=-1
        mapping = {nums[0]: 0}

        for i in range(1,len(nums)):
            if target - nums[i] in mapping:
                return [mapping[target-nums[i]],i]
            mapping[nums[i]]=i
        return [index1,index2]
def combine(arr1, arr2):
    ans = []
    i=0;j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        elif arr1[i]==arr2[j]:
            ans.append(arr1[i])
            ans.append(arr2[j])
            i+=1
            j+=1
        else:
            ans.append(arr2[j])
            j+=1
    while i < len(arr1):
        ans.append(arr1[i])
        i+=1
    while j < len(arr2):
        ans.append(arr2[j])
        j+=1
    return ans


def sortedSquares( nums: List[int]) -> List[int]:


    nums = [abs(i) for i in nums]
    nums.sort() # O(n*(log(n)))
    nums = [i*i for i in nums]
    return nums



print(Problems().twoSum([2,7,11,15],9))
print(Problems().twoSum([3,2,4],6))
strs = ["eat","tea","tan","ate","nat","bat"]
print(Problems().groupAnagrams(strs))
print(sortedSquares([-4,-1,0,1,4,5]))