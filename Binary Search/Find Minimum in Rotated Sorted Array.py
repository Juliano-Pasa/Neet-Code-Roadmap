from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        minimum = nums[0]

        while l < r:
            mid = (l + r) // 2
            idxNext = (mid + 1) % len(nums)

            if nums[mid] > nums[idxNext]:
                return nums[idxNext]
            if nums[mid] <= minimum:
                minimum = nums[mid]
                r = mid
            else:
                l = mid + 1

        return minimum