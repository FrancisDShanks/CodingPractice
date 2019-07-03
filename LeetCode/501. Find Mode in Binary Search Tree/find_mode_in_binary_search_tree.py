# solution - 1
# use dict to count all appearence
# use extra O(n) space, but faster
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        d = {}
        self.max_cnt = 0
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            d[node.val] = (d[node.val] + 1) if node.val in d.keys() else 1
            if d[node.val] > self.max_cnt:
                self.max_cnt = d[node.val]
            inorder(node.right)
        
        inorder(root)

        res = []
        for k,v in d.items():
            if v == self.max_cnt:
                res.append(k)
        return res
        
        
        
# solution - 2 
# for the follow up question, do not use extra space
# take use of the property of the BST, the nodes are in order, or say all values in inorder travesal of the BST is continuous
# when a value is visited, all it appearence in the BST are found, it can be easily counted.
# 开始的想法是过两遍,第一遍找出maximum_count, Mode的长度, 第二遍找出所有的Mode(s)
# 后来看了别人的解法, 可以只过一次遍历就行,每次找到'最长'的就加到result,遇到新的长度就清空result.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        
        self.max_cnt = 0
        self.res = []
        self.cnt = 0
        self.pre = sys.maxsize
        
        def inorder(node):
            if not node:
                return
            # traverse left subtree
            inorder(node.left)
            # deal with the node
            if node.val == self.pre:
                self.cnt += 1
            else:
                self.cnt = 1
                self.pre = node.val
                
            if self.cnt > self.max_cnt:
                self.max_cnt = self.cnt
                self.res = [node.val]
            elif self.cnt == self.max_cnt:
                self.res.append(node.val)
            #traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return self.res
        
        
# solution - 3 
# iterative solution of solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
from collections import deque
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        
        max_cnt = 0
        res = []
        cnt = 0
        pre = sys.maxsize
        
        s = deque()
        cur = root
        while cur or s:
            if not cur:
                cur = s.pop()
                
                if cur.val == pre:
                    cnt += 1
                else:
                    pre = cur.val
                    cnt = 1
                if cnt == max_cnt:
                    res.append(cur.val)
                if cnt > max_cnt:
                    max_cnt = cnt
                    res = [cur.val]
                
                
                cur = cur.right
            else:
                s.append(cur)
                cur = cur.left
        return res
