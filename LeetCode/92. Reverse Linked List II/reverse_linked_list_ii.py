class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for _ in range(m-1):
            cur = cur.next
        pointer = cur.next
        # notice here: should be range(n-m) not range(n-m+1)
        # when m=2, n=4
        # 1 - 2 - 3 - 4 - 5 => 1 - 4 - 3 - 2 - 5
        # three numbers involved but only two steps happend
        # the 'pointer' is not moved, just other numbers move from pointer's right to pointer's left
        for _ in range(n-m):
            tmp = cur.next
            cur.next = pointer.next
            pointer.next = pointer.next.next
            cur.next.next = tmp
        
        return dummy.next
            
