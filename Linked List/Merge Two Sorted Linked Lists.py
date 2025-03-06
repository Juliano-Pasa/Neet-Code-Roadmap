from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head = None
        current = None

        if not list1:
            head = list2
            list2 = list2.next
        elif not list2:
            head = list1
            list1 = list1.next
        elif list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        if not head:
            return None
        
        current = head
        while list1 or list2:
            if not list1:
                current.next = list2
                current = current.next
                list2 = list2.next
            elif not list2:
                current.next = list1
                current = current.next
                list1 = list1.next
            elif list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        return head