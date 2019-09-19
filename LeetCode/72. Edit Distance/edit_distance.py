# 9/19/2019 - DP with cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = dict() # use a dict to store dps
            
        def dp(i, j):
            # don't do duplicate works
            if (i, j) in m.keys():
                return m[(i, j)]
            
            # boundary case
            if i < 0 or j < 0:
                return max(i, j) + 1
            
            # same chars, edit distance is 0
            if word1[i] == word2[j]:
                tmp = dp(i - 1, j - 1)
            else:
                tmp = min(dp(i - 1, j) + 1, # add one char to w1
                          dp(i, j - 1) + 1, # delete one char in w1 = add one to w2
                          dp(i - 1, j -1) + 1) # replace
            m[(i, j)] = tmp
            return tmp
        
        return dp(len(word1) - 1, len(word2) - 1)
            
# 9/19/2019 - DP table
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp table, only store the previous level
        l1 = len(word1) + 1
        l2 = len(word2) + 1
        
        # boundary case
        pre = [j for j in range(l2)]
        
        for i in range(1, l1):
            # cur[0] always = i, boundary case
            cur = [i for _ in range(l2)]
            for j in range(1, l2):
                # 整个循环里面i和j的坐标都错了一位的,因为都有一个为空的行/列
                # word[i-1]==word2[j-1]时cur[j]=pre[j-1]
                # word[i-1]!=word2[j-1]时cur[j]=pre[j-1]+1,相当于replace操作
                cur[j] = min(pre[j - 1] + (word1[i - 1] != word2[j - 1]), 
                             pre[j] + 1, # j也就是word2少一个,相当于对word1做insert操作
                             cur[j - 1] + 1) # 对word1做delete操作
            pre = cur[:]
        return pre[-1]
            









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
