from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}

        for i in range(len(nums)):
            subtraction = target - nums[i]
            if subtraction in numSet:
                return [numSet[subtraction], i]
            numSet[subtraction] = i

        pair = [0, 0]
        for i in range(len(nums)):
            if nums[i] in numSet:
                if numSet[nums[i]] == i:
                    continue
                pair[0] = i
                pair[1] = numSet[nums[i]]
                break

        if pair[0] > pair[1]:
            aux = pair[0]
            pair[0] = pair[1]
            pair[1] = aux
        
        return pair
