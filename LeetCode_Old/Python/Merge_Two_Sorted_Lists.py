# -*- coding: utf-8 -*-
'''
Created on Feb 06, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        l3 = ListNode(0)
        head = l3
        while l1 and l2:
            if l1.val<l2.val:
                l3.next = l1
                l1=l1.next
            else:
                l3.next = l2
                l2=l2.next
            l3=l3.next           
        if l1:
            l3.next=l1
        elif l2:
            l3.next=l2       
        return head.next
            
    
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    h1=l1
    l1.next = ListNode(4)
    l1=l1.next
    l1.next = ListNode(6)
    l1=l1.next
    l1.next = ListNode(7)
    l1=l1.next
    l1.next = ListNode(11)
    l1=l1.next
    
    l2 = ListNode(2)
    h2=l2
    l2.next = ListNode(8)
    l2=l2.next
    l2.next = ListNode(9)
    l2=l2.next
    l2.next = ListNode(10)
    l2=l2.next
    l2.next = ListNode(12)
    l2=l2.next
    

    h3 = s.mergeTwoLists(h1,h2)
    while h3:
        print h3.val,
        h3=h3.next
