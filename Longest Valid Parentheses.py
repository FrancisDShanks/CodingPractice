class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        #use a stack to store the position of each '('
        stack = []
        #the longest result
        res = 0
        #a mark to store the start position of current valid parentheses, only update when the stack is empty and the current char is ')'
        #because in such situation, this ')' can never be paired
        start = 0
        for i in range(0,len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i]==')':
                if len(stack)!= 0 and s[stack[len(stack)-1]]=='(':
                    stack.pop()
                    res = max(res,i-start+1 if len(stack)==0 else i-stack[len(stack)-1])
                else:
                    start = i+1
        return res
