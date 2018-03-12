import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        q1 = queue.Queue()
        q2 = queue.Queue()
        q1.put(root)
        while not q1.empty():
            cur = q1.get()
            # Notice: None can be put in queue, so child node must be checked here
            if cur.left:
                q2.put(cur.left)
            if cur.right:
                q2.put(cur.right)
            if q1.empty():
                result.append(cur.val)
                q1 = q2
                q2 = queue.Queue()
        return result

if __name__ == "__main__":
    s = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    rl = r.left
    rl.right = TreeNode(5)
    rr = r.right
    rr.right = TreeNode(4)
    print(s.rightSideView(r))
