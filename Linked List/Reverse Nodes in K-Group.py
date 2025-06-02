from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        previousHead = head
        previousGroup = None
        newHead = None

        while True:
            previous = None
            current = previousHead
            
            i = 0
            while current and i < k:
                nextNode = current.next
                current.next = previous
                previous = current
                current = nextNode

                i += 1

            if i == k:
                if not previousGroup:
                    newHead = previous
                else:
                    previousGroup.next = previous
                previousGroup = previousHead

                previousHead.next = current
                previousHead = current
            
            else:
                current = previous
                previous = None
                while i > 0:
                    nextNode = current.next
                    current.next = previous
                    previous = current
                    current = nextNode

                    i -= 1
                break
        return newHead    
