from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while len(stack) and temp > stack[-1][0]:
                idx = stack[-1][1]
                result[idx] = i - idx
                stack.pop()
            stack.append((temp, i))

        return result
