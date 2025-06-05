from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, minimum, maximum):
        if not root:
            return True
        
        if root.val <= minimum or root.val >= maximum:
            return False

        left = self.dfs(root.left, minimum, root.val)
        right = self.dfs(root.right, root.val, maximum)
        
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-INF"), float("INF"))
        