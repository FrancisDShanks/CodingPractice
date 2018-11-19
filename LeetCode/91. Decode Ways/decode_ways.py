class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this is a DP problem
        # the algorithm is
        # ways[i] = w[i-1] + w[i-2] if number 's[i-1]s[i]' in range [1,26]
        #         = w[i-1] else
        #
        # w[i-1] means how many decode ways for s[0:i]
        # 1. treat s[i] as a single digit character (0~9), the decode ways equals to decode ways of w[i-1], plus a isolated single digit character
        # 2. if number 's[i-1]s[i]' in range [1,26], the decode ways equals to decode ways of w[i-2], plus a two digit character
        #
        # Notice that, when len(s)=2, the w[1] = w[0] + w[-1], it is a correct result
        # Pay attention to '0's
        if s[0]=='0':return 0
        w = [1 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]=='0' and (s[i-1]!='1' and s[i-1]!='2'):
                return 0
            check = int(s[i-1:i+1])
            if check>9 and check <27:
                if s[i]=='0' and (s[i-1]=='1' or s[i-1]=='2'):
                    w[i] = w[i-2]
                else:
                    w[i] = w[i-1] + w[i-2]
            else:
                w[i] = w[i-1]
        return w[len(s)-1]
            
            
# a faster solution is do not use list
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for i
        # a represents dp[i-1]
        # b represents dp[i-2]
        if s[0]=='0':return 0
        a, b = 1, 0
        for i in range(1,len(s)):
            if s[i]=='0':
                if s[i-1] not in '12':
                    return 0
                a, b = 0, a
            
            elif s[i-1]=='1' or s[i-1]=='2' and int(s[i])<7:
                a, b = a + b, a
            else:
                a, b = a + b, 0
        return a + b   
