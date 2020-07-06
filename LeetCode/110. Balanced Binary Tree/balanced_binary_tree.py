# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root)[0]
    
    def helper(self, node):
        if not node:
            return (True, 0)
        
        isleft, heightleft = self.helper(node.left)
        isright, heightright = self.helper(node.right)
        
        if isleft and isright and abs(heightleft - heightright) < 2:
            return (True, max(heightright, heightleft) + 1)
        
        return (False, 0)
