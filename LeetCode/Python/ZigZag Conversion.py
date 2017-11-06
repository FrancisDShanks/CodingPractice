class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows<0:
            return
        if nRows == 1:
            return s
        if nRows >= len(s):
            return s
        
        #get the number of parts and size of each part
        size = (nRows-1)*2
        parts = len(s)/size
        if parts*size < len(s): parts+=1
        
        
        #separate the string into parts
        #like a string has 14 chars should be parse as 4 parts:
        #1  2  3  4
        #1 12 23 34
        #11 22 33
        #1  2  3
        #bound is a list store beginning element of each part
        bound=[]
        for i in range(0,parts):
            bound.append(i*size)
        
        res = ""
        #row 1
        for i in range(0,parts):
            res+=s[bound[i]]
        #row 2~n-1
        for j in range(1,nRows-1):
            for i in range(0,parts):
                if bound[i]+j<len(s):
                    res+=s[bound[i]+j]
                if bound[i]+size-j<len(s):
                    res+=s[bound[i]+size-j]
        #row n
        for i in range(0,parts):
            if bound[i]+nRows-1<len(s):
                res+=s[bound[i]+nRows-1]
        return res
