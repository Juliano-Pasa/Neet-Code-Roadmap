class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, biggest):
        if not root:
            return 0
        
        left = self.dfs(root.left, max(biggest, root.val))
        right = self.dfs(root.right, max(biggest, root.val))

        if root.val >= biggest:
            return left + right + 1
        return left + right

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)