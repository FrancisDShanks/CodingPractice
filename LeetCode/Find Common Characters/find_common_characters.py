class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        from collections import Counter
        cnt = dict(Counter(A[0]))
        for i in range(1, len(A)):
            tmp = dict(Counter(A[i]))
            for key in list(cnt.keys()):
                if key not in tmp:
                    del cnt[key]
                elif cnt[key] > 0 or tmp[key] > 0:
                    cnt[key] = min(cnt[key], tmp[key])
        ret = []
        for k,v in cnt.items():
            ret.extend(k * v)
        return ret
        
        
        
# found another solution which is brilliant taken advantage of python features
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        results = []
        i = 0
        while i <= len(A[0]) - 1:
            if all(A[0][i] in item for item in A):
                results.append(A[0][i])
                A = [item.replace(A[0][i], '', 1) for item in A]
                i -= 1
            i += 1
        return results
