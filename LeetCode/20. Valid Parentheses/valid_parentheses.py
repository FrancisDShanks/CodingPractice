# just use stack and pay attention to details
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        left = ['(', '[', '{']
        for i in s:
            # handle left
            if i in left:
                stack.append(i)
                continue
                # handle right
            if len(stack) == 0:
                return False
            prev = stack.pop()
            if (prev == '(' and i == ')') or (prev == '[' and i == ']') or (prev == '{' and i == '}'):
                continue
            return False
        if len(stack) > 0:
            return False
        return True