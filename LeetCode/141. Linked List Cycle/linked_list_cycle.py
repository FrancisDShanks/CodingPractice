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
        p1, p2 = head, head
        while p2.next and p2.next.next:    
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False
            
            
