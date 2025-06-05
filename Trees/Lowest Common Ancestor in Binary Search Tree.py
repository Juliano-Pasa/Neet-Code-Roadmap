class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if p.val > q.val:
            p, q = (q, p)
        
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
