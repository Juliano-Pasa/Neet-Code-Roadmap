from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)

        for num in nums:
            numCount[num] += 1
        
        occurences = [[] for _ in range(len(nums) + 1)]
        for num in numCount:
            occurences[numCount[num]].append(num)

        i = len(occurences)
        result = []
        while k > 0:
            i -= 1
            if len(occurences[i]) == 0:
                continue

            result.extend(occurences[i])
            k -= len(occurences[i])

        return result