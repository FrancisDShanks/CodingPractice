"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# using two queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        import Queue
        res = []
        tmp = []
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put(root)
        while (not q1.empty()) or (not q2.empty()): 
            if q1.empty():
                res.append(tmp)
                tmp = []
                q1,q2 = q2,q1
            else:
                cur = q1.get()
                tmp.append(cur.val)
                for c in cur.children:
                    q2.put(c)
        # don't forget the last level nodes should be put in the result
        res.append(tmp)
        return res
