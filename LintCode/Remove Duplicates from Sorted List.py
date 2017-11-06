#Working on Link Code
#Author:Francis Du
#Date:  02/29/2016
#Problem: Remove Duplicates from Sorted List
#Things needs to be noticed:
#               1. None list    2.only one node   3.duplicate at the head  4.duplicate at the tail

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy.next
        while (cur is not None) and (cur.next is not None):
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
                
