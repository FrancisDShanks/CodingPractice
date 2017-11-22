class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        term = '1'
        for _ in range(n-1):
            #notice here!!!!!!!!!!!!!!
            count = 0
            curchar = term[0]
            countchar = curchar
            newterm = ''
            for j in range(0, len(term)):
                curchar = term[j]
                if j == len(term) - 1:
                    if countchar == curchar:
                        count += 1
                    else:
                        newterm += (str(count) + countchar)
                        count = 1
                    newterm += (str(count) + curchar)
                    
                else:
                    if countchar == curchar:
                        count += 1
                    else:
                        newterm += (str(count) + countchar)
                        #notice here!!!!!!!!!!!!!! should reset to 1
                        count = 1
                        countchar = curchar
            term = newterm
                        
        return term
                
                
#possible solutions
    using re
    using groupby
