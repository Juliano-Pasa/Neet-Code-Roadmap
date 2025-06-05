from queue import Queue
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []

        q = Queue()
        q.put(root)

        while not q.empty():
            levelValues = []
            nextQ = Queue()
            while not q.empty():
                node = q.get()
                levelValues.append(node.val)

                if node.left:
                    nextQ.put(node.left)
                if node.right:
                    nextQ.put(node.right)

            q = nextQ
            result.append(levelValues)
        
        return result