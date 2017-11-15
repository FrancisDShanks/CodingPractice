#straight foward solution
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        
        if not t.left and not t.right:
            return str(t.val)
         
        if t.left:
            tleft = '(' + self.tree2str(t.left) + ')'
        else:
            tleft = '()'
            
        if t.right:
            tright = '(' + self.tree2str(t.right) + ')'  
        else:
            tright = '' 
        return str(t.val) + tleft + tright
