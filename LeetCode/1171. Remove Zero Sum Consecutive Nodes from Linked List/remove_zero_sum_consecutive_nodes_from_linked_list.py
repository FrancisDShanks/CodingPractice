# 记录下每个结点,从head结点加到当前结点处整个链表值得总和
# 比如 给的例子 []1,2,-3,3,1]
# 加一个dummy头结点方便操作,node: 0,1,2,-3,3,1
# 计算的head到每个结点的和   sum: 0,1,3, 0,3,4
# 那么删除的结点的逻辑是:
#    每当计算出一个新的和值
#    如果是第一次出现,记录下这个求得这个和值得当前节点
#    如果之前出现过,那么之前出现的结点a,这次重复出现的结点b,就要删除a之后一直到b的所有点,也就是a->next=b->next
#    比如例子的dummy结点和值是0 ,到(-3)这个点第二次出现和值0,则删掉1,2,-1这些点
# 显然用哈希表记录这些和值最合适
# 再举一个例子:
#注释一个字母 a b c  d  e f g  h  i j
#链表本身:    2 5 1 -4 -2 3 6 -2 -4 1
# 加dummy   0 2 5 1 -4 -2 3 6 -2 -4 1
# 和值      0 2 7 8  4  2  5 11 9 5 6
# b和值与e和值一样,删掉cde,f和值与i和值一样,删掉ghi
# 所以最后剩下的链表是 a-b-f-j
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        visit_sum = {}
        visit_sum[0] = dummy
        cur = dummy.next
        prev_sum = 0
        while cur:
            cur_sum = prev_sum + cur.val
            if cur_sum in visit_sum:
                visit_sum[cur_sum].next = cur.next
            else:
                visit_sum[cur_sum] = cur
            cur = cur.next
            prev_sum = cur_sum
        return dummy.next
        
        
