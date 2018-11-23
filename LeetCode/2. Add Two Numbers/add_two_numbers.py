# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    # Not difficult, but easy to leave bug, double check carefully
    def addTwoNumbers(self, l1, l2):
        if l1==None: return l2
        if l2==None: return l1
        res = ListNode(0)
        tmpres = res
        more = 0
        while l1 and l2:
            tmpres.next = ListNode((l1.val+l2.val+more)%10)
            more = (l1.val+l2.val+more)//10
            l1=l1.next
            l2=l2.next
            tmpres = tmpres.next
        if l2:
            while l2:
                tmpres.next = ListNode((l2.val+more)%10)
                more = (l2.val+more)//10
                l2=l2.next
                tmpres=tmpres.next
        elif l1:
            while l1:
                tmpres.next = ListNode((l1.val+more)%10)
                more = (l1.val+more)//10
                l1=l1.next
                tmpres=tmpres.next
        if more>0:
            tmpres.next = ListNode(more)
        return res.next
