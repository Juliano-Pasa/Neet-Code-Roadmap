from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val <= other.val

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for node in lists:
            heapq.heappush(heap, node)

        head = ListNode()
        current = head

        while len(heap) > 0:
            nextNode = heapq.heappop(heap)    
            current.next = nextNode
            current = nextNode

            if nextNode.next != None:
                heapq.heappush(heap, nextNode.next)
        return head.next
