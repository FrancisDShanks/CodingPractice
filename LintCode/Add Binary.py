class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        if a is None: return b
        if b is None: return a
        
        a = a[::-1]
        b = b[::-1]
        
        c = ""
        extra=0
        
        if len(a)<len(b):
            for i in range(len(a),len(b)):
                a = a + '0'
        else:
            for i in range(len(b),len(a)):
                b = b + '0'
                
            
        for i in range(0,len(a)):
            if a[i] == '1' and b[i] == '1':
                if extra==1:
                    c = c + '1'
                    extra=1
                else:
                    c = c + '0'
                    extra=1
            elif a[i]=='0' and b[i]=='0':
                if extra==1:
                    c = c + '1'
                    extra=0
                else:
                    c = c + '0'
                    extra=0
            else:
                if extra==1:
                    c = c + '0'
                    extra=1
                else:
                    c = c + '1'
                    extra=0
                    
        if extra==1:
            c = c + '1'
        c = c[::-1]
        return c
