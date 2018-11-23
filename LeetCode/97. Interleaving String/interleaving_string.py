# dynamical programming 
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        c = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        c[0][0] = True
        
        for i in range(1,l1 + 1):
            if s1[i-1] == s3[i-1]:c[i][0] = True
            else:break
                
        for j in range(1,l2 + 1):
            if s2[j-1] == s3[j-1]:c[0][j] = True
            else:break
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s1[i-1] == s3[i+j-1] and c[i-1][j]:
                    c[i][j] = True
                if s2[j-1] == s3[i+j-1] and c[i][j-1]:
                    c[i][j] = True
        return c[l1][l2]
            
