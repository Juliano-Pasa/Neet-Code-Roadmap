from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        maximumStack = []
        maximumIdx = 0

        for i, v in enumerate(nums):
            while len(maximumStack) > maximumIdx and v > maximumStack[-1]:
                maximumStack.pop()
            maximumStack.append(v)

            if i >= k - 1:
                if i - k >= 0 and maximumStack[maximumIdx] == nums[i - k]:
                    maximumIdx += 1
                result.append(maximumStack[maximumIdx])

        return result