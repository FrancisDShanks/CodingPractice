# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inOrder(self,node):
        if node is None:
            return []
        return (self.inOrder(node.left) + [node.val] + self.inOrder(node.right))
         
        
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        l = self.inOrder(root)
        mindif = l[1] - l[0]
        for i in range(2,len(l)):
            if l[i] - l[i-1] < mindif:
                mindif = l[i] - l[i-1]
        return mindif
