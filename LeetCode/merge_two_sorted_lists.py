# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curNode = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                curNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curNode.next = ListNode(l2.val)
                l2 = l2.next
            curNode = curNode.next
            
        if l1:
            curNode.next = l1
        elif l2:
            curNode.next = l2
        return dummyHead.next
            
