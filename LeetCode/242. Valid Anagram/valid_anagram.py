# first solution - take advantage of Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
        
        
# second solution - we can use dict to do the same thing
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for c in s:
            if c in d1.keys():
                d1[c] += 1
            else:
                d1[c] = 1
                
        for c in t:
            if c in d2.keys():
                d2[c] += 1
            else:
                d2[c] = 1
        return d1==d2
        
# solution - 3
# also, we can use a list with length of 26(or 52) to counter all letters appearence
