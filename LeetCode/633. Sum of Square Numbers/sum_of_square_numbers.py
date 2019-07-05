import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c)) + 1
        low = 0
        high = n
        while low <= high:
            tmp = low * low + high * high
            if tmp == c:
                return True
            elif tmp > c:
                high -= 1
            else:
                low += 1
        return False
