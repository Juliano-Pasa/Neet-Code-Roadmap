from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1):
            aux = nums1
            nums1 = nums2
            nums2 = aux

        totalSize = len(nums1) + len(nums2)
        target = (totalSize) // 2

        left = 0
        right = len(nums2) + 1

        while left < right:
            mid = (left + right) // 2

            leftNums1 = nums1[target-mid-1] if target-mid-1 >=0 else float("-infinity")
            rightNums1 = nums1[target-mid] if target-mid < len(nums1) else float("infinity")
            leftNums2 = nums2[mid-1] if mid-1 >= 0 else float("-infinity")
            rightNums2 = nums2[mid] if mid < len(nums2) else float("infinity")

            if leftNums2 <= rightNums1 and leftNums1 <= rightNums2:
                if totalSize % 2 == 1:
                    return min(rightNums1, rightNums2)
                return (max(leftNums1, leftNums2) + min(rightNums1, rightNums2)) / 2
                
            elif leftNums2 > rightNums1:
                right = mid
            else:
                left = mid + 1