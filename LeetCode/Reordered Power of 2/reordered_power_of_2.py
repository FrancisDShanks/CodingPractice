from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # if 1 <= N <= 10 ** 9: return False
        power = int(math.log2(10**9) + 1)
        powers = (2**i for i in range(power))
        cnt = Counter(str(N))
        len_n = len(str(N))
        for i in powers:
            p = str(i)
            if len(p) > len_n:
                return False
            if cnt == Counter(p):
                return True
        return False
            
            
        
            
