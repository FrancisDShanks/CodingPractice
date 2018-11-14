# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        ret = ListNode(0)
        ret.next = head
        pointer = head
        while pointer.next:
            cur = ret.next
            ret.next = pointer.next
            pointer.next = pointer.next.next
            ret.next.next = cur
        return ret.next
