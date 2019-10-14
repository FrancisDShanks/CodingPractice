# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 因为a和b有共同的部分
# 假设a由aa与c组成
#     b由bb与c组成
# 分别把b放到a之后和a放到b之后构成新的链表
# d = b+a = bb+c+aa+c
# e = a+b = aa+c+bb+c
# 可以想到d长度=e长度, 且两者最后部分都是c
# 所以按一次走一步遍历d与e,两者会同时到达在题目所求的汇合点

# 对a和b没有共同部分的情况
# d = b+a = bb+aa
# e = a+b = aa+bb
# 两者会同时到达链表尾部

# 所以算法就是一次走一步遍历b+a和a+b,看d和e相同时的情况

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while not a == b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a if a else None
        
        
