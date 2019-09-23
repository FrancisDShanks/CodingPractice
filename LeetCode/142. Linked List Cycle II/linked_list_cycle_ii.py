# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 这种解法是用额外空间的,比较直接容易想到,用一个字典保存出现过的node,第一个重复的一定就是环的起点
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        d = dict()
        node = head
        while node:
            if node.val not in d:
                d[node.val] = [node]
            else:
                if node in d[node.val]:
                    return node
                else:
                    d[node.val].append(node)
            node = node.next
        return None
        
        
#O(1)额外空间的解法应该是两个快慢指针先找到相遇的点,在用两个每次走一步的指针分别从链表头和相遇点开始走,两个指针相遇的地方就是环开始的地方.

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1, p2 = head, head
        while True:    
            if not p2.next or not p2.next.next:
                return None
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        
        p1 = head
        while True:
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                return p1
            
