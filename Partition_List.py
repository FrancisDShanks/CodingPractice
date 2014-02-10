# -*- coding: utf-8 -*-
'''
Created on Feb 07, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        #if list has no elements or only one, just return
        if head is None or head.next is None:
            return head
        #put the first element directly to the new list
        #record the head and the tail of the sorted list
        h = head
        tail=h
        #start insertion sort from the second element
        head=head.next
        h.next=None
        #go through the unsorted list
        while head!=None:
            tmp = h
            #if this node is smaller or equal to the head of the sorted list, set this node as new head
            if head.val<=h.val:
                t=head
                head=head.next
                t.next = h
                h=t
            #if this node is larger or equal to the tail of the sorted list, set this node as new tail
            elif head.val>=tail.val:
                tail.next=head
                head=head.next
                tail=tail.next
                tail.next=None
            #else, find the position and insert
            else:
                pre = tmp
                tmp=tmp.next
                while tmp!=None:
                    if head.val<=tmp.val:
                        t=head
                        head=head.next
                        t.next=tmp
                        pre.next = t 
                        break
                    pre=tmp
                    tmp=tmp.next

        return h

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(5)
    h1=l1
    l1.next = ListNode(7)
    l1=l1.next
    l1.next = ListNode(2)
    l1=l1.next
    l1.next = ListNode(4)
    l1=l1.next
    l1.next = ListNode(6)
    l1=l1.next
    
    
    h3 = s.insertionSortList(h1)
    
    while h3:
        print h3.val,
        h3=h3.next
