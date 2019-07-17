class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        seq = text.split(' ')
        if len(seq) < 3: return []
        ret = []
        for i in range(2,len(seq)):
            if seq[i - 2] == first and seq[i - 1] == second:
                ret.append(seq[i])
        return ret
