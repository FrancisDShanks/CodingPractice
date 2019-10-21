# 根据中序遍历找第k个,找到就返回
# follow up的情况,BST频繁更新,可以在中序遍历时候存下前k个为counts,然后更新这个counts
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        s = list()
        cur = root
        cnt = 0
        while s or cur:
            if not cur: 
                cur = s.pop()
            else:
                while cur.left:
                    s.append(cur)
                    cur = cur.left
            
            cnt += 1
            if cnt == k:
                return cur.val
            
            cur = cur.right
        
            
            
        
