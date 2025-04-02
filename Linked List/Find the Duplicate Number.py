from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return fast
    
nums = [1,2,3,2,2]
solution = Solution()
print(solution.findDuplicate(nums))