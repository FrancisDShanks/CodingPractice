# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:            
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        
        
#notice the defination of 'leaf' node
#have to check if the node is 'leaf' node or not
