# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sums(self,node):
        if node is None:
            return []
        if (node.left is None) and (node.right is None):
            return [str(node.val)]
        tmp = self.sums(node.left) + self.sums(node.right)
        tmp = [s+str(node.val) for s in tmp]
        return tmp
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.sums(root)
        res = 0
        for num in l:
            res += int(num[::-1])
        return res
        
