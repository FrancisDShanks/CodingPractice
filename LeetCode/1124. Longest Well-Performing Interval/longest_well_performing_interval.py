from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ret = []
        for i in arr2:
            ret.extend([i] * c[i])
            del c[i]
        if c:            
            tmp = []
            for k, v in c.items():             
                tmp.extend([k] * v)
            tmp.sort()
            ret.extend(tmp)
        return ret
       
       
# same idea, different implement
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx = {n: i for i, n in enumerate(arr2)}
        tmp = [[] for _ in range(len(arr2))]
        rest = []
        for i, n in enumerate(arr1):
            if n in idx:
                tmp[idx[n]].append(n)
            else:
                rest.append(n)
        return [row[i] for row in tmp for i in range(len(row))] + sorted(rest)
