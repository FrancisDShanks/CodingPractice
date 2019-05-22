class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if x > 1:
            tmp = 1
            while tmp < bound:
                tmp = tmp * x
                xpower.append(tmp)
            xpower.pop()
          
        ypower = [1]
        if y > 1:
            tmp = 1
            while tmp < bound:
                tmp = tmp * y
                ypower.append(tmp)
            ypower.pop()
        
        result = set()
        lenypower = len(ypower)
        for xx in xpower:
            index = 0
            while index < lenypower:
                if xx + ypower[index] <= bound:
                    result.add(xx + ypower[index])
                else:
                    break
                index += 1
        return list(result)
