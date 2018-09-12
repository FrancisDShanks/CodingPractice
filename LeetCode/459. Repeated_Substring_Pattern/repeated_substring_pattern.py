class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l==1:return False
        # only check substring with len 1-len(s)//2+1
        for i in range(1,l//2+1):
            # skip substring whose length cannot be divided by len(s)
            if l%i != 0:
                continue
            # check if there is a pattern
            if s[:i]*(l//i) == s:
                return True
        return False
                
                
        
