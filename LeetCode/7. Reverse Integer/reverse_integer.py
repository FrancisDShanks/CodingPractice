class Solution:
    # @return an integer
    def reverse(self, x):
        s=str(x)
        sign = ''
        if s[0]=='+' or s[0]=='-':
            sign = s[0]
            s=s[1:]
        length = len(s)
        news = ''
        for i in range(length):
            news = s[i] + news
            
        newx = int(sign+news)
        if newx >= - 2 ** 31 and newx <= 2**31-1:
            return newx
        else:
            return 0
            
