# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        

# -------------------------------------------------------------------------------
        
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        cur = root
        while cur.left:
                stack.append(cur.left)
                cur = cur.left
                
        while cur and stack:            
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                cur = cur.right
                stack.append(cur)
                while cur.left:
                    stack.append(cur.left)
                    cur = cur.left
                
            
        return res
        
        
        
# -------------------------------------------------------------------------------

class Solution:
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
            
