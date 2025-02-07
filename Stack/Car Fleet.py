from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posTime = []

        for i in range(len(position)):
            posTime.append((position[i], (target - position[i]) / speed[i]))

        posTime.sort()
        resultStack = []

        for _, time in posTime:
            while len(resultStack) and time >= resultStack[-1]:
                resultStack.pop()
            resultStack.append(time)

        return len(resultStack)
