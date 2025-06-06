from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        nodes = {root.val: root}

        pIdx = 1
        iIdx = 0

        size = len(preorder)
        previous = root
        nextLeft = preorder[0] != inorder[0]

        while pIdx < size:
            node = TreeNode(preorder[pIdx])
            
            if nextLeft:
                previous.left = node
            else:
                previous.right = node
            nodes[node.val] = node

            if preorder[pIdx] != inorder[iIdx]:
                nextLeft = True
                previous = node
            else:
                nextLeft = False
                while iIdx < size and inorder[iIdx] in nodes:
                    previous = nodes[inorder[iIdx]]
                    iIdx += 1
            pIdx += 1
        
        return root
