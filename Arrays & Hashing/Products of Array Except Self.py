from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preffix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            preffix[i] = preffix[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = preffix[i] * suffix[i]
        
        return result

