# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# first step is to calculate the depth of all node
# second step is to find the result 
# for a node, if largest_depth(node.left) == largest_depth(node.right)
# then the node is the root of the result subree
# or, the subtree will be in the node.left(if its depth is larger) or node.right
# use a dict to store the depth to avoid duplicate recurrsion


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0
        self.d = {}
        def trans(node):
            if not node:
                return 0
            self.d[node] = max(trans(node.left) + 1, trans(node.right) + 1)
            return self.d[node]
        self.d[root] = trans(root)
        return self.helper(root)
    
    def helper(self, node):
        if not node or (not node.left and not node.right):
            return node
        elif not node.left and node.right:
            return self.helper(node.right)
        elif not node.right and node.left:
            return self.helper(node.left)
        elif self.d[node.left] == self.d[node.right]:
            return node
        elif self.d[node.left] > self.d[node.right]:
            return self.helper(node.left)
        else:
            return self.helper(node.right)
            
            
