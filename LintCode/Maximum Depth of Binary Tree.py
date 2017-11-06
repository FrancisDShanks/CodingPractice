# Author -  Francis
# 03/04/2016

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        
        if root is None:
            return 0
            
        #if root.left == None and root.right == None:
        #    return 1
        
        return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1
