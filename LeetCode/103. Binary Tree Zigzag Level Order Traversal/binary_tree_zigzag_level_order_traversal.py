# basically this problem is a modified binary tree level order traversal problem
# just maintain a zigzag mark to zigzag it

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
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
        zigzag = 1
        while dq:
            cur = dq.popleft()
            if cur is None:
                if zigzag:
                    res.append(lvl)
                    zigzag = 0
                else:
                    res.append(lvl[::-1])
                    zigzag = 1
                lvl = []
                if dq:
                    dq.append(None)
            else:
                lvl.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
        return res
