# A simple math problem
# more mathematical solution is just res = int(math.sqrt(8*n+1)//2-1)
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        tmp = n
        while tmp >= 0:
            res += 1
            tmp -= res
            
        if n == res*(res+1)/2:
            return res
        return res - 1
