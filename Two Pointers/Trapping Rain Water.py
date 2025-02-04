from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        preffix = [0] * len(height)
        suffix = [0] * len(height)

        for i in range(1, len(height)):
            preffix[i] = max(preffix[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i+1])

        totalWater = 0
        for i in range(len(height)):
            if height[i] >= preffix[i] or height[i] >= suffix[i]:
                continue
            totalWater += min(preffix[i], suffix[i]) - height[i]

        return totalWater

