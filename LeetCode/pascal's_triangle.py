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

    
    
    #improvement:
    #       use a temp list to store the previous line of pascal's triangle
    #       accessing 1-dimension array is much faster than accessing 2-dimension array
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
            pre = ret[i - 1]
            cur = [1]
            for j in range(1,i):
                cur.append(pre[j - 1] + pre[j])
            cur.append(1)
            ret.append(cur)
        return ret
    
    
    #an elegant solution using map(), modified from leetcode discuss
    #apply the idea: A row can be constructed by offset sum of the previous row
    #    1 3 3 1 0
    #  + 0 1 3 3 1
    #  = 1 4 6 4 1
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            res.append([j for j in map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])])
        return res[:numRows]
