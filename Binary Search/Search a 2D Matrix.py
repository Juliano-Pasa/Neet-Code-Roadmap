from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        while l != r:
            mid = (l + r) // 2

            if target >= matrix[mid][0]:
                l = mid + 1
            else:
                r = mid

        idx = l - 1
        if idx < 0:
            return False
        
        l = 0
        r = len(matrix[idx])
        while l < r:
            mid = (l + r) // 2

            if target == matrix[idx][mid]:
                return True
            elif target < matrix[idx][mid]:
                r = mid
            else:
                l = mid + 1
        return False