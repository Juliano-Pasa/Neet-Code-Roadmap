from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        head = l1
        carry = 0

        while l1 and l2:
            result = l1.val + l2.val + carry
            l1.val = result % 10
            carry = result // 10

            previous = l1
            l1 = l1.next
            l2 = l2.next        

        if l1:
            while carry and l1:
                result = l1.val + carry
                l1.val = result % 10
                carry = result // 10

                previous = l1
                l1 = l1.next
        elif l2:
            previous.next = l2
            while carry and l2:
                result = l2.val + carry
                l2.val = result % 10
                carry = result // 10

                previous = l2
                l2 = l2.next

        if carry:
            previous.next = ListNode(carry, None)

        return head
    
