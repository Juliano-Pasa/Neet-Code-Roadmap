from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set([])
        nums = sorted(nums)
        
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            addition = nums[i] + nums[j] + nums[k]

            while j < k:
                if addition == 0:
                    triplets.add(tuple([nums[i], nums[j], nums[k]]))
                    k -= 1
                elif addition > 0:
                    k -= 1
                else:
                    j += 1
                addition = nums[i] + nums[j] + nums[k]

        result = []
        for triplet in triplets:
            result.append(list(triplet))
        return result
