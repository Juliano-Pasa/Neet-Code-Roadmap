from queue import Queue
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        q = Queue()
        q.put(root)

        while not q.empty():
            nextQ = Queue()
            while not q.empty():
                node = q.get()

                if node.left:
                    nextQ.put(node.left)
                if node.right:
                    nextQ.put(node.right)
            
            q = nextQ
            result.append(node.val)

        return result