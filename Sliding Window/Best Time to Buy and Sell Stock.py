from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maximumProfit = 0
        right = len(prices) - 1
        left = right - 1

        while left >= 0:
            sell = prices[right]
            buy = prices[left]

            if sell <= buy:
                right = left
            else:
                maximumProfit = max(maximumProfit, sell - buy)
            left -= 1

        return maximumProfit
