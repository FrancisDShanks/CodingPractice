class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        b = s.split()
        if not b:
            return 0
        c = b.pop()
        return len(c) if c.isalpha() else 0
        
        
        
        
        
#solution without python built-in func
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        count = 0
        precount = 0
        for i in range(0,len(s)):
            if s[i] == ' ' and count:
                precount = count
                count = 0
            elif s[i] != ' ':
                count += 1
        return count if count else precount
