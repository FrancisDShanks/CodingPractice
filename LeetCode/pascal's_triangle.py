class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #return [] if numRows < 1
        if numRows < 1:
            return []
        
        #hard code the first line
        ret = [[1]]
        #loop to generate 2nd line to numRows line
        for i in range(1,numRows):            
            cur = [1]
            for j in range(1,i):
                cur.append(ret[i - 1][j - 1] + ret[i - 1][j])
            cur.append(1)
            ret.append(cur)
        return ret
