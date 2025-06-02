from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = []
        qStack = []

        pStack.append(p)
        qStack.append(q)

        while len(pStack) > 0 and len(qStack) > 0:
            pCurrent = pStack.pop()
            qCurrent = qStack.pop()

            if (pCurrent and not qCurrent) or (not pCurrent and qCurrent):
                return False
            
            if not (pCurrent or qCurrent):
                continue

            if pCurrent.val != qCurrent.val:
                return False
            
            pStack.append(pCurrent.right)
            pStack.append(pCurrent.left)
            qStack.append(qCurrent.right)
            qStack.append(qCurrent.left)

        return True
        