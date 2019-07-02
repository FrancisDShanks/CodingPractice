# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# a modified question from remove node from linked list
# copy node.next to node and delete the node.next
# that is why the question exclude the tail node which do not have node.next
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tmp = node.next
        node.next = tmp.next
        node.val = tmp.val
        
