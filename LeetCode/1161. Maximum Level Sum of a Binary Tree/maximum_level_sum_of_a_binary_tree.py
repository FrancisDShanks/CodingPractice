# using a queue to level order traverse the tree with a marker
# or can use two queues to level order traverse the tree



# one queue with a marker
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        mark = "marker"
        q = deque([root, mark])
        level = 1
        res, maxsum = 1, root.val
        tmp_sum = 0     
        while len(q):
            h = q.popleft()
            if h == mark:   
                print(level, tmp_sum)
                if tmp_sum > maxsum:
                    res, maxsum = level, tmp_sum
                level += 1
                tmp_sum = 0
                if len(q):
                    q.append(mark)
            else:
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
                tmp_sum += h.val
        return res
        
        

# two queues
# this solution is faster
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q1 = [root]
        q2 = []
        res, max_sum = 1, root.val
        level = 1
        while len(q1):
            cur_sum = 0
            for node in q1:
                cur_sum += node.val
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if cur_sum > max_sum:
                res, max_sum = level, cur_sum
            level += 1
            q1, q2 = q2, []
        return res
            
