class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in range(0,len(s)):
            ret += s[len(s) - i - 1]
        return ret
        
