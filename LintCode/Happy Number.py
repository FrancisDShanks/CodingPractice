#Author : Francis Du
#03/14/2016
#use hash map to reduce search time
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        if n<=0:
            return False
        d = {}
        while True:
            if n == 1:
                return True
            else:
                if d.has_key(n):
                    return False
            
            d[n] = 0
            s = 0
            r = 0
            while n>0:
                r = n % 10
                n = n / 10
                s = s + r * r
            n = s
                
                
                
