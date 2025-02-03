from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        sequences = {}

        for num in nums:
            if num in sequences:
                continue
            if num - 1 not in values:
                sequences[num] = 1
                continue

            current = 1
            while num - current in values:
                if num - current in sequences:
                    current += sequences[num - current]
                    break
                
                sequences[num - current] = 1
                current += 1

            sequences[num] = current

        longest = 0
        for num in sequences:
            if sequences[num] > longest:
                longest = sequences[num]
        
        return longest
