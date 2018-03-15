# AC beats 36.98%
# convert to int, take advantage of number operation like mod operation and divide
# easy to implement but slower
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i = len(a) - 1
        j = len(b) - 1
        plus = 0
        while i >= 0 or j >= 0 or plus == 1:
            if i >= 0:
                plus += int(a[i])
            if j >= 0:
                plus += int(b[j])
            res = str(plus % 2) + res
            i -= 1
            j -= 1
            plus = plus // 2
        return res