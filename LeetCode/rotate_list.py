# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 1:
            return head
        nhead = None
        ntail = None
        tail = None
        length = 0
        cur = head
        
        #find the tail of the linked list
        while cur:
            length += 1
            if cur.next == None:
                tail = cur
            cur = cur.next
        
        #find the new head and the new tail
        k = k % length
        if not k or length == 1:
            return head
        k = length - k
        cur = head
        for i in range(1,k):
            cur = cur.next
        ntail = cur
        nhead = cur.next
        
        #rotate
        tail.next = head
        ntail.next = None
        head = nhead
        return head

    
    #almost the same sulotion
    #build and cut a circle instead of record the new head/tail location
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k < 1:
            return head
        tail = None
        length = 0
        cur = head
        
        #find the tail of the linked list
        while cur:
            length += 1
            if cur.next == None:
                break
            cur = cur.next
            
        k = k % length
        if not k or length == 1:
            return head
        #connect the tail and head to build a circle
        cur.next = head
        
        #find the new head and the new tail
        k = length - k
        cur = head
        for i in range(1,k):
            cur = cur.next
        
        #cut the circle to build the rotated result
        head = cur.next
        cur.next = None
        return head
