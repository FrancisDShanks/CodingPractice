# 因为是链表又要求nlogn时间复杂度和常数级空间复杂度
# 可以排除用快排思路,冒泡选择思路,桶或者堆也不合适,转换成其他数据结构也不合适
# 很容易想到应该尝试mergesort的思路

class Solution:    
    def sortList(self, head: ListNode) -> ListNode:
        # merge 
        def merge(h1, h2):
            d = ListNode(0)
            cur = d
            while h1 and h2:
                if h1.val < h2.val:
                    cur.next = h1
                    h1 = h1.next
                else:
                    cur.next = h2
                    h2 = h2.next
                cur = cur.next

            if h1:
                cur.next = h1
            if h2:
                cur.next = h2
            return d.next
        # end of merge
        
        if not head or not head.next: 
            return head

        
        s, f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        h2 = s.next
        s.next = None
        return merge(self.sortList(head), self.sortList(h2))
        
# 不限制空间复杂度的版本,运行结果要快很多
# 多用O(n)的空间,速度快一倍还要多
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
            
        nodes = sorted(nodes, key=lambda x:x.val)
        d = ListNode(0)
        cur = d
        for node in nodes:
            cur.next = node
            cur = cur.next
        cur.next = None
