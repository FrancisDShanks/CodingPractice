# solution 1 : iterative with two stacks
# solution 2 : iterative with one stack
# solution 3 : iterative with one stack

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

# 另一种单栈的算法,和solution 2本质上一样:
# 和inorder算法一样入栈顺序是node.right,node
# 一直访问当前结点的左子树,直到当前为空
# 栈顶元素出栈,这里和inorder不一样的是,判断出栈元素的右子树和新的栈顶元素是否一样
# 如果一样,就说明当前结点的右子树还没有访问,就把栈顶(当前的右子树)出栈,当前结点再入栈,处理结点的右子树
# 再一次访问到这个结点时,出栈元素的右子树和新的栈顶元素不一样,说明右子树处理过了
# solution - 3
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
        s1 = []
        res = []
        cur = root
        while s1 or cur:
            # push cur.right and cur, keep DFS cur.left
            while cur:
                if cur.right:
                    s1.append(cur.right)
                s1.append(cur)
                cur = cur.left
            
            # when cur is None, pop stack
            cur = s1.pop()
            # if cur.right == s1[-1], means the right subtree of cur need to visit first
            if cur.right and s1 and cur.right == s1[-1]:
                # pop out the 'right subtree'
                s1.pop()
                # push back the cur node
                s1.append(cur)
                # visit the right subtree
                cur = cur.right
            # if else means the cur node don't have right node or right subtree has been visited, vist cur node
            else:
                res.append(cur.val)
                cur = None
        return res
                
