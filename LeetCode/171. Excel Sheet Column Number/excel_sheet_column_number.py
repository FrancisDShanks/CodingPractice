class Solution:
    def titleToNumber(self, s: str) -> int:
        tens = 1
        ret = 0
        index = len(s)
        while index > 0:
            ret += (ord(s[index - 1]) - 64) * tens
            tens *= 26
            index -= 1
        return ret
            
