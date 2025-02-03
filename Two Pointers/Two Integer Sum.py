from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        addition = numbers[left] + numbers[right]
        while addition != target:
            if addition > target:
                right -= 1
            else:
                left += 1
            addition = numbers[left] + numbers[right]

        return [left+1, right+1]