#the hard part is the algorithm not the coding
#search Levenshtein distance algorithm from google

#solution using dynamic progamming with O(mn) space
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for j in range(0,l2 + 1)] for i in range(0,l1 + 1)]
        for i in range(0,l1 + 1):
            dp[i][0] = i
        for j in range(0,l2 + 1):
            dp[0][j] = j
            
        for i in range(0,l1):
            for j in range(0,l2):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j] + 1
                dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j+1]+1,dp[i+1][j]+1)
                
        return dp[-1][-1]
        
        
        
#solution using O(n)
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        l1, l2 = len(word1), len(word2)
        pre = [0 for _ in range(l2 + 1)]
        for j in range(0,l2 + 1):
            pre[j] = j
        for i in range(l1):
            cur = [i+1]*(l2 + 1)
            for j in range(l2):
                cur[j+1] = min(cur[j]+1, pre[j+1]+1, pre[j]+(word1[i]!=word2[j]))
            pre = cur[:]
        return pre[-1]    
