# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# using slow/fast pointers to find cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p1 = head
        p2 = head.next
        while p1 and p2:
            if p1 == p2:
                return True
            p1 = p1.next
            if not p2.next:
                return False
            p2 = p2.next.next
        return False
            
            
