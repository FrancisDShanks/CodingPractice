# 题目简单,主要就在于问清楚要求和场景,对时间复杂度有没有有求,对空间复杂度有没有要求,允不允许改变原链表的结构
# 比如O(n)time O(1)space的解法就会改变原链表,如果不改变的话还需要再翻转回去,就要跑3趟

# O(n) time and O(1) space
# 快慢指针找到中点, 翻转中点之后的一半,和前一半比较是否一样
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def findmid(head):
            dummy = ListNode(-1)
            dummy.next = head
            slow = fast = dummy
            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # reverse linked list after node(not include node)
        def reverse_after(node):
            if node.next is None:
                return
            last = node.next
            cur = last.next
            while cur:
                last.next = cur.next
                cur.next = node.next
                node.next = cur
                cur = last.next
            return 
        
        mid = findmid(head)
        reverse_after(mid)
        # 从mid的下一个开始和头部开始比,直到mid到尾部
        # 如果是奇数个节点会多出原始的mid这个点,正好略掉(前半比后半多一个)
        mid = mid.next
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True

# O(n) time and O(n) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l == list(reversed(l))
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return all([l[i] == l[-i-1] for i in range(len(l)//2)])
