# a basic DP problem
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<=1 or n<=1:
            return 1
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                if i==0 or j==0:
                    res[i][j]=1
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
