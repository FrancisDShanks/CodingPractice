# 这样写同样是递归,代码用的算法完全一样, 速度快了很多
# 原因是将helper函数嵌套定义在sumOfLeftLeaves函数里面,值得玩味

class Solution:
    

        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(node):
            if not node:
                return 
            if node.left:
                if not node.left.left and not node.left.right:
                    self.res += node.left.val
                else:
                    helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)
        return self.res
        
