#just need to know the algorithm to convert from 10-base to 7-base
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'
        isPositive = False if num < 0 else True
        num = abs(num)
        res = []
        while num:
            res.append(num % 7)
            num = num // 7
        ret = ''.join([str(i) for i in reversed(res)])
        return ret if isPositive else ('-' + ret)
