from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxSum = float("-INF")

    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        sums = [root.val, root.val + left, root.val + right, root.val + left + right, self.maxSum]

        self.maxSum = max(sums)
        upper = max(sums[:-2])

        return upper

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxSum