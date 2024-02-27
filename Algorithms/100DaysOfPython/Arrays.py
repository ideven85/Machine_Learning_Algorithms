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

print(Problems().twoSum([2,7,11,15],9))
print(Problems().twoSum([3,2,4],6))
strs = ["eat","tea","tan","ate","nat","bat"]
print(Problems().groupAnagrams(strs))