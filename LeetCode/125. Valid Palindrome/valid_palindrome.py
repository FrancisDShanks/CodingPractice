# didn't use python's build-in str functions
# 'a'-'z' : 97-122
# 'A'-'Z' : 65-90
# '0'-'1' : 48-57
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        while l<r:
            s1 = ord(s[l])
            s2 = ord(s[r])
            if 65<=s1 and s1<=90:
                s1 += 32
            if 65<=s2 and s2<=90:
                s2 += 32
            if (s1<97 or s1>122) and (s1<48 or s1>57):
                l+=1
                continue
            if (s2<97 or s2>122) and (s2<48 or s2>57):
                r-=1
                continue  
            if s1!=s2:
                return False
            l+=1
            r-=1
        return True
        
