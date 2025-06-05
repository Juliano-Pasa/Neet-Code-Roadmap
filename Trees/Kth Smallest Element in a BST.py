from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.smallest = -1

    def dfs(self, root, k, previous):
        if not root:
            return 0
        
        left = self.dfs(root.left, k, previous)
        if left + previous + 1 == k:
            self.smallest = root.val
            return left + previous + 2
        
        if left + previous + 1 > k:
            return left + previous + 1
        
        right = self.dfs(root.right, k, left + previous + 1)
        return left + right + 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k, 0)
        return self.smallest