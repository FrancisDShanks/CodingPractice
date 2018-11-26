# solution 1 : iterative with two stacks
# solution 2 : iterative with one stack

# solution - 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        s1 = [root]
        s2 = []
        while s1:
            cur = s1.pop()
            s2.append(cur)
            if cur.left:
                s1.append(cur.left)
            if cur.right:
                s1.append(cur.right)
        res = []
        while s2:
            res.append(s2.pop().val)
        return res
        

# solution - 2
# much faster than two stacks
# maintain a prev pointer to record the previous visited node
# 因为入栈顺序是 node, node.right, node.left
# 所以如果prev是node的左子树/右子树,就说明node的子树都访问过了,就该node出栈了
# 访问到叶子结点,就出栈
# 否则就把node的左右子树入栈
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        s1 = [root]
        prev = None
        res = []
        while s1:
            cur = s1[-1]
            if (not cur.left and not cur.right) or (prev and (prev==cur.left or prev==cur.right)):
                s1.pop()
                res.append(cur.val)                
                prev = cur
                continue
            if cur.right:
                s1.append(cur.right)
            if cur.left:
                s1.append(cur.left)
        return res
