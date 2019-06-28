# 本质上就是LCS最长公共子序列的问题, 返回的结果就是两个字符串的长度和减去2*LCS长度
# 用动态规划求解
# LCS[i][j] represents the length of LCS of string word1[:i] and string word2[:j]
# LCS[i][j] = LCS[i-1][j-1] + 1, if word1[i] == word[j]
#           = max(LCS[i][j-1], LCS[i-1][j], if word1[i] != word[j]
# Notice:
# 考虑string为空的情况,单独处理,用动规跑结果会错
# 写动规注意数组边界判断

# Solution - 1
class Solution:
    def LCSLen(self, w1, w2):
        lcs_len = [[0 for j in range(len(w2))] for i in range(len(w1))]
        if w1[0] == w2[0]:
            lcs_len[0][0] = 1
        for i in range(1, len(w1)):
            if w2[0] == w1[i]:
                lcs_len[i][0] = 1
            else:
                lcs_len[i][0] = lcs_len[i-1][0]
        for j in range(1, len(w2)):
            if w1[0] == w2[j]:
                lcs_len[0][j] = 1
            else:
                lcs_len[0][j] = lcs_len[0][j-1]
        for i in range(1, len(w1)):
            for j in range(1, len(w2)):
                
                if w1[i] == w2[j]:
                    lcs_len[i][j] = lcs_len[i-1][j-1] + 1
                else:
                    lcs_len[i][j] = max(lcs_len[i-1][j], lcs_len[i][j-1])
        return lcs_len[len(w1) - 1][len(w2) - 1]
                    
    def minDistance(self, word1: str, word2: str) -> int: 
        if word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        return len(word1) + len(word2) - (self.LCSLen(word1, word2) * 2)
            

# Solution - 2
# optimized from solution 1, use 1-dimension list to save memory usage
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if not word1 or not word2:
            return max(len(word1), len(word2))

        lcs_len = [0] * len(word2)
        
        for i in range(0, len(word1)):
            temp = [0] * len(word2)
            for j in range(0, len(word2)):
                               
                if word1[i] == word2[j] and not j:
                    temp[j] = 1
                elif word1[i] == word2[j]:
                    temp[j] = lcs_len[j-1] + 1
                else:
                    temp[j] = max(lcs_len[j], temp[j-1])
            lcs_len = temp
            
        return len(word1) + len(word2) - (2 * lcs_len[-1])
                    

            
