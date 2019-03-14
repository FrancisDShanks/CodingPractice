class Solution:
    def customSortString(self, S: str, T: str) -> str:
        if not S or not T:
            return T
        from collections import Counter
        d = Counter(T)
        res = []
        for s in S:
            if s in d.keys():
                res.append(s*d.pop(s))
        for key,item in d.items():
            res.append(key*item)
        return ''.join(res)
            
        
