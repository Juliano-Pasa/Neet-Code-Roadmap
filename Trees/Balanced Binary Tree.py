from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.dfs(root)

        return self.balanced
    
    def dfs(self, root):
        if not root or not self.balanced:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if abs(left - right) > 1:
            self.balanced = False
            return 0
        
        return 1 + max(left, right)
        