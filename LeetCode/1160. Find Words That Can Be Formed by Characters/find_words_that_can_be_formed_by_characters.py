from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_counter = Counter(chars)
        for w in words:
            mark = True
            c = Counter(w)
            for k, v in c.items():
                if k not in chars_counter or v > chars_counter[k]:
                    mark = False
                    break
            if mark:
                res += len(w)
        return res
        
        
        
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_counter = Counter(chars)
        for w in words:
            c = Counter(w)
            if all([k in chars_counter and v <= chars_counter[k] for k, v in c.items()]):
                res += len(w)
        return res
