# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(before,after):
            # head->...->before->reverse0->...->reversek->after->...->tail
            # reverse reverse0 to reversek
            last = before.next
            cur = last.next
            for _ in range(1,k):
                last.next = cur.next
                cur.next = before.next
                before.next = cur
                cur = last.next
            return last
        
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        before = dummy
        count = 0
        
        while head:
            count += 1
            if count%k == 0:
                # reverse (before,head.next)
                # set the last node of the reversed part as new before
                before = reverse(before,head.next)
                head = before.next
            else:
                head = head.next
        return dummy.next
            
        
