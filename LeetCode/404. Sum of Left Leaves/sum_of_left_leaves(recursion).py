# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion solution
    def helper(self, node):
        if node is None:
            return 
        if node.left:
            if not node.left.left and not node.left.right:
                self.res += node.left.val
            else:
                self.helper(node.left)
        if node.right:
            self.helper(node.right)
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res
        
        
        
