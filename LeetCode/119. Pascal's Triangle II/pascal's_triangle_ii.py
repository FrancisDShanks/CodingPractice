class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(1,rowIndex + 1):
            pre = [j for j in ret]
            ret[0] = 1
            for j in range(1,i):
                ret[j] = pre[j - 1] + pre[j]
            ret.append(1)
        return ret
            
