# backtrack solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pars = '('
        
        def helper(pars, n1, n2):
            if n1 == 0 and n2 == 1:
                res.append(pars + ')')
                return
            if n1 > 0:
                helper(pars + '(', n1 - 1, n2)
            if n2 > 1 and n2 > n1:
                helper(pars + ')', n1, n2 - 1)
            return
        helper(pars, n-1, n)
        return res
        
        
# another backtrack solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(pars, n1, n2):
            if len(pars) == 2 * n:
                res.append(pars)
                return
            if n1 < n:
                helper(pars + '(', n1 + 1, n2)
            if n2 < n1:
                helper(pars + ')', n1, n2 + 1)
            return
        
        helper('', 0, 0)
        return res
