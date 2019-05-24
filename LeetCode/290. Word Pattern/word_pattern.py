class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        s = str.split(' ')
        # make sure the length of pattern is equal to words count of str
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d.keys():
                # make sure the same pattern must match same word
                if d[pattern[i]] != s[i]:
                    return False
            else:
                # make sure the different pattern must match different word
                if s[i] in d.values():
                    return False
                d[pattern[i]] = s[i]
        return True               
                       
                
