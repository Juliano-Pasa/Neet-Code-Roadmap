from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootStack = []
        subRootStack = []

        rootStack.append(root)
        subRootStack.append(subRoot)

        while len(rootStack) > 0 and len(subRootStack) > 0:
            currentRoot = rootStack.pop()
            currentSubRoot = subRootStack.pop()

            if (not currentRoot and currentSubRoot) or (currentRoot and not currentSubRoot):
                return False
            if not (currentRoot or currentSubRoot):
                continue
            if currentRoot.val != currentSubRoot.val:
                return False

            rootStack.append(currentRoot.right)
            rootStack.append(currentRoot.left)
            subRootStack.append(currentSubRoot.right)
            subRootStack.append(currentSubRoot.left)

        return not (len(rootStack) or len(subRootStack))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootStack = []
        rootStack.append(root)

        while len(rootStack) > 0:
            currentRoot = rootStack.pop()

            if not currentRoot:
                continue

            if currentRoot.val == subRoot.val:
                sameTree = self.isSameTree(currentRoot, subRoot)
                if sameTree:
                    return True

            rootStack.append(currentRoot.right)
            rootStack.append(currentRoot.left)

        return False