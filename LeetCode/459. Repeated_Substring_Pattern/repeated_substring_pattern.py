class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l==1:return False
        for i in range(0,l//2):
            sub = s[:i+1]
            lsub = len(sub)

            if l%lsub != 0:
                continue

            if sub*(l//lsub) == s:
                return True
        return False
                
        
