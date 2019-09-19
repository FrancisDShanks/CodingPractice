# dp with memory
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = dict()
        
        def dp(i, j):
            if (i, j) in m:
                return m[(i, j)]
            
            if i == -1 or j == -1:
                tmp = 0                
            elif text1[i] == text2[j]:
                tmp = dp(i - 1, j - 1) + 1
            else:
                tmp = max(dp(i - 1, j), dp(i, j - 1))
            m[(i, j)] = tmp
            return tmp
        
        return dp(len(text1) - 1, len(text2) - 1)
        
        
        
# dp table
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0 for i in range(l1 + 1)] for j in range(l2 + 1)]
        
        for i in range(0, l2):
            for j in range(0, l1):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            
            
        
        return dp[-1][-1]
        
        
#dp table only store previous level
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        prv = [0 for _ in range(l1 + 1)]
        
        for i in range(0, l2):
            cur = [0 for _ in range(l1 + 1)]
            for j in range(0, l1):
                if text1[j] == text2[i]:
                    cur[j + 1] = prv[j] + 1
                else:
                    cur[j + 1] = max(prv[j + 1], cur[j])
            prv = cur[:]
        return prv[-1]
