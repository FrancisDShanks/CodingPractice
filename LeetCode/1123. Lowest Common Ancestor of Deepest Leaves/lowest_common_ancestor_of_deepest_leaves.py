# basically the same problem as [865. Smallest Subtree with all the Deepest Nodes]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None
            l = dfs(node.left)
            r = dfs(node.right)
            if l[0] == r[0]:
                return l[0] + 1, node
            elif l[0] > r[0]:
                return l[0] + 1, l[1]
            else:
                return r[0] + 1, r[1]
            
        return dfs(root)[1]
