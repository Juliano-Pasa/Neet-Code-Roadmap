from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        previousNode = head
        current = head.next
        head.next = None

        while current:
            nextNode = current.next
            current.next = previousNode
            previousNode = current
            current = nextNode

        return previousNode