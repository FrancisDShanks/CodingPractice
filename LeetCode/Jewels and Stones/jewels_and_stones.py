# prettty easy problem, lots of possible solutions
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set(J)
        cnt = 0
        for st in S:
            if st in j:
                cnt += 1
        return cnt
        
        
from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set(J)
        cnt_s = Counter(S)
        return sum([v if k in j else 0 for k, v in cnt_s.items()])
        
        
#using reges matching is much slower    
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len(re.findall('[' + J + ']', S))
        
