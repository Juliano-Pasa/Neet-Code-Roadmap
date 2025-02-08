from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) + 1

        while l != r:
            k = (l + r) // 2

            hours = sum(map(lambda x : ceil(x / k), piles))

            if h >= hours:
                r = k
            else:
                l = k + 1
        
        return l