# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
# notice that all nodes in the left subtree must be smaller than root
# so it is wrong if only check root.val > root.left.val
# the algorithem have check the subtree's value bound:
# (-maxsize,root.val) for left subtree
# (root.val, maxsize) for right subtree
class Solution:
    def check(self,node,up,down):
        if not node:
            return True
        if node.val >= up or node.val <=down:
            return False
        return self.check(node.left,node.val,down) and self.check(node.right,up,node.val)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root.left,root.val,-sys.maxsize) and self.check(root.right,sys.maxsize,root.val)

        
