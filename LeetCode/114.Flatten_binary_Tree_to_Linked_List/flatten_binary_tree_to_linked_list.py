# 递归处理,先左子树,后右子树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_sub(root)
        
    def flatten_sub(self, root):
        if not root:
            return root
        if not root.left and not root.right:
            return root, root
        
        node = root
        left = node.left
        right = node.right
        
        #flatten left subtree
        if left:
            head, tail = self.flatten_sub(node.left)
            node.left = None        
            node.right = head
            tail.right = right
            node = tail
        
        #faltten right subtree
        if right:
            head, tail = self.flatten_sub(node.right)      
            node.right = head
        
        return root, tail
        
        
