# solution - 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            index = t.find(c)
            if index == -1:
                return False
            t = t[index + 1:]
        return True
            

# solution - 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
        if i == len(s):
            return True
        return False
