class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sym = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        scale = 1000
        res = ''
        for i in range(6,-1,-2):
            digit = num//scale
            if digit != 0:
                if digit <= 3:
                    res += digit * sym[i]
                elif digit == 4:
                    res += sym[i]
                    res += sym[i + 1]
                elif digit == 5:
                    res += sym[i + 1]
                elif digit <= 8:
                    res += sym[i + 1]
                    res += sym[i] * (digit - 5)
                elif digit == 9:
                    res += sym[i]
                    res += sym[i+2]
            num = num % scale
            scale //= 10
        
        return res
