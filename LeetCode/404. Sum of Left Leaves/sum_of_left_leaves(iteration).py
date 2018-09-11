# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # iteration solution
        # no need to care about the order, so using two list as level order traversal
        if not root:
            return 0
        res = 0
        q1 = [root]
        q2 = []
        while q1:
            for node in q1:
                if node.left:
                    # if node.left is a leaf node
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                    else:
                        q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2
            q2 = []
        return res
