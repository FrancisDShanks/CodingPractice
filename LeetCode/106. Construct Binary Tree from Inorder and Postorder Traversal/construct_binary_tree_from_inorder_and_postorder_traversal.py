# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:            
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        loc = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:loc], postorder[:loc])
        root.right = self.buildTree(inorder[loc + 1:], postorder[loc:-1])
        return root
