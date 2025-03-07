from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        currentNode = head

        while currentNode:
            count += 1
            currentNode = currentNode.next
        
        midNode = head
        mid = count // 2

        while mid > 0:
            mid -= 1
            midNode = midNode.next

        previousNode = midNode
        currentNode = midNode.next
        previousNode.next = None

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        currentForward = head
        currentBackward = previousNode

        for i in range(count//2):
            nextForward = currentForward.next
            currentForward.next = currentBackward
            currentForward = nextForward

            if i != count//2 - 1:
                nextBackward = currentBackward.next
                currentBackward.next = nextForward
                currentBackward = nextBackward
