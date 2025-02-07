from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightStack = []
        leftMins = [0] * len(heights)
        rightMins = [0] * len(heights)

        for i in range(len(heights)):
            while len(heightStack) and heights[i] < heightStack[-1][0]:
                idx = heightStack[-1][1]
                leftMins[idx] = i - idx - 1

                heightStack.pop()
            heightStack.append((heights[i], i))
            
        for _, idx in heightStack:
            leftMins[idx] = len(heights) - 1 - idx

        heightStack = []
        for i in range(len(heights) - 1, -1, -1):
            while len(heightStack) and heights[i] < heightStack[-1][0]:
                idx = heightStack[-1][1]
                rightMins[idx] = idx - i - 1

                heightStack.pop()
            heightStack.append((heights[i], i))

        for _, idx in heightStack:
            rightMins[idx] = idx

        maxArea = 0
        for i in range(len(heights)):
            area = (leftMins[i] + rightMins[i] + 1) * heights[i]
            maxArea = max(area, maxArea)
        
        return maxArea