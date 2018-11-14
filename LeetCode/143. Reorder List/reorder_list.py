# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # part 1 - find the middle point and devide the list to two lists
        slow, fast = head, head
        head2 = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
            
        # part 2 - reverse the second part
        dummy = ListNode(0)
        dummy.next = head2
        pointer = dummy.next
        while pointer.next:
            tmp = dummy.next
            dummy.next = pointer.next
            pointer.next = pointer.next.next
            dummy.next.next = tmp
        head2 = dummy.next
        
        # part 3 - merge two list
        ret = ListNode(0)
        cur = ret
        while head and head2:
            cur.next = head
            cur = cur.next
            head = head.next
            cur.next = head2
            cur = cur.next
            head2 = head2.next
        if head:
            cur.next = head
        elif head2:
            cur.next = head2
        head = ret.next
        return
        
        
# or part 3 can be:
        # part 3 - merge two list
        cur = head
        while cur and head2:
            tmp = head2
            head2 = head2.next
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        if head2:
            cur.next = head2
        return
        
        
