# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 很简单的快慢指针 在链表头加了一个dummy方便思考...
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.next
        
        
            
            
