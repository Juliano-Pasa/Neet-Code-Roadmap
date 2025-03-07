from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        currentNode = head

        while currentNode:
            count += 1
            currentNode = currentNode.next
        
        if count == n:
            head = head.next
            return head

        previousNode = None
        currentNode = head

        while count > n:
            previousNode = currentNode
            currentNode = currentNode.next
            count -= 1

        previousNode.next = currentNode.next

        return head