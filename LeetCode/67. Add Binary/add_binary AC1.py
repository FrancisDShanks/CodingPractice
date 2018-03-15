# AC beats 82.11%
# did not convert string to int
# faster, but more code to write
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        res = ''
        add = '0'
        for i in range(0, len(a)):
            if a[i] == '0' and b[i] == '0':
                res = res + add
                add = '0'
            elif a[i] == '1' and b[i] == '1':
                res = res + add
                add = '1'
            else:
                if add == '0':
                    res = res + '1'
                    add = '0'
                else:
                    res = res + '0'
                    add = '1'

        index = len(a)
        while add == '1' and index < len(b):
            if b[index] == '0':
                res = res + '1'
                add = '0'

            else:
                res = res + '0'
                add = '1'
            index += 1
        res = res + b[index:]
        if add == '1':
            res = res + '1'
        return res[::-1]