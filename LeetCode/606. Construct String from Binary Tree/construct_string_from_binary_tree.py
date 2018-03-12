#straight foward solution using recursion
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

    
    
    
    
    
#using the idea of stack, do the pre-order 
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        stack = [t]
        ret = ''
        
        while stack:
            pop = stack.pop()
            if pop == '(' or pop == ')':
                ret += pop
            else:
                if not pop.left and not pop.right:
                    ret += str(pop.val)
                else:
                    ret += str(pop.val)
                    if pop.right:
                        stack.append(')')
                        stack.append(pop.right)
                        stack.append('(')
                        
                    stack.append(')')
                    if pop.left:
                        stack.append(pop.left)
                    stack.append('(')

        return ret
    
    
    
    
    #4-lines solution from leetcode discussion, using the same algorithm as my 1st solution
    class Solution:
    def tree2str(self, t):
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)
