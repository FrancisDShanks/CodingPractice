# 两个solution,第一个直接访问结点,左右子树都入栈
# 第二个,访问结点,把访问过的结点入栈,然后访问结点的左子树.如果没有左子树就出栈,访问出栈结点的右子树.(栈中结点都是已经被访问过左子树的)
# 第二个solution理论上入栈出栈的操作会少一些,并采用了迭代器
# solution - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        if not root: return s
        s.append(root)
        res = []
        while s:
            cur = s.pop()
            res.append(cur.val)
            if cur.right:
                s.append(cur.right)
            if cur.left:
                s.append(cur.left)
        return res
            
        
# solution - 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(self.preTrav(root))
    
    def preTrav(self,root):
        if not root:return
        cur = root
        s = []
        while cur or s:
            if cur:
                yield cur.val
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                cur = cur.right
