# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root==None:
            return True
        l=self.inOrder(root)
        for i in range(1,len(l)):
            if l[i]<=l[i-1]:
                return False
        return True
        
    def inOrder(self,root):
        l=[]
        if root.left:
            l+=self.inOrder(root.left)
        l+=[root.val]
        if root.right:
            l+=self.inOrder(root.right)
        return l
        
