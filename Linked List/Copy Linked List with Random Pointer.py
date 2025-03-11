from collections import defaultdict
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random        

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNodes = []
        oldNodes = {}

        current = head
        idx = 0
        while current:
            newNodes.append(Node(current.val))
            oldNodes[current] = idx

            current = current.next
            idx += 1

        newNodes.append(None)
        current = head
        idx = 0
        
        while current:
            newNodes[idx].next = newNodes[idx+1]

            if current.random != None:
                newNodes[idx].random = newNodes[oldNodes[current.random]]
            current = current.next
            idx += 1

        return newNodes[0]
    
