from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        l = 0
        r = size * 2
        previousNum = 0
        previousDir = -1

        while l < r:
            mid = (l + r) // 2
            idx = mid % size

            if target == nums[idx]:
                return idx
            
            if previousDir == 0 and nums[idx] > previousNum:
                l = mid + 1
            elif previousDir == 1 and nums[idx] < previousNum:
                r = mid
            elif target < nums[idx]:
                previousNum = nums[idx]
                previousDir = 0
                r = mid
            else:
                previousNum = nums[idx]
                previousDir = 1
                l = mid + 1

        return -1
