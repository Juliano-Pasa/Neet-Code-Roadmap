from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head.next

        while hare:
            if hare == turtle:
                return True

            if not hare.next:
                return False
            hare = hare.next.next
            turtle = turtle.next

        return False