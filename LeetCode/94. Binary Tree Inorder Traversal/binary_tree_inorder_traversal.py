# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
# recurrsion is easy
# here is iteration solution
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p = root
        stack = []
        res = []
        while p or stack:
            if not p:
                p = stack.pop()
                res.append(p.val)
                p = p.right
            else:
                stack.append(p)
                p = p.left
        return res
            
