# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        dq = collections.deque()
        dq.append(root)
        dq.append(None)
        lvl = []
        while dq:
            cur = dq.popleft()
            if cur is None:
                res.append(lvl)
                lvl = []
                if dq:
                    dq.append(None)
            else:
                lvl.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
        return res[::-1]
