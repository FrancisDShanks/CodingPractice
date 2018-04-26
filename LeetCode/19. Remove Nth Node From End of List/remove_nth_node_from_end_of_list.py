# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # say L is the length of the linked list.
        # the n-th node, which is n-1 step to the end node. 
        # To remove the n-th node, we find the (n+1)th from the end is more convinence.
        # when pright reach the tail, pleft.next is node to be removed
        # than the (n+1)th node from the end has n step to the end.
        # so we use two pointers the distance of which is n steps to do this
        # Pay attention to the case that the removed node is at the head/tail
        pleft, pright = head, head
        for _ in range(n):
            if not pright.next: # in case of n=L
                return head.next
            pright = pright.next
        
        while pright.next:
            pleft=pleft.next
            pright=pright.next
        
        pleft.next = pleft.next.next
        return head
        
