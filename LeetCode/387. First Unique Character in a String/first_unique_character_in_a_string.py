class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use a dict to count letters
        # if the letter appears the first time, record the location
        # if the letter appeared before, set the value to -1
        d = dict()
        
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] = -1
            else:
                d[s[i]] = i
        
        # maximum possible location is len(s)-1
        res = len(s)
        for key in d.keys():
            if d[key] is not -1:
                res = min(res,d[key])
        return res if res != len(s) else -1
