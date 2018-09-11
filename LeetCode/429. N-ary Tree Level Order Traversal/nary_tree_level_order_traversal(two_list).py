"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# using two list instead of two queue. should be faster
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        res = []
        q1 = [root]
        while q1: 
            tmp = []
            q2 = []
            for node in q1:
                tmp.append(node.val)
                for c in node.children:
                    q2.append(c)
            q1 = q2
            res.append(tmp)
        return res
