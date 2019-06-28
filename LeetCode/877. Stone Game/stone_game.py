# 可以用dp或者带历史记录的dfs做, 或者直接return true 也能过... 
# solution - dp
class Solution:
    def stoneGame(self, piles) -> bool:
        #dp[i][j] = max(dp[i][j-1] + p[j], dp[i+1][j] + p[i])
        #dp[i][i+1] = max(p[i], p[i+1]) for i in range(n)
        n = len(piles)
        cnt = sum(piles)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        def calculate_dp(i, j):
            if not dp[i][j]:
                if i + 1 == j:
                    dp[i][j] = max(piles[i], piles[j])
                else:
                    dp[i][j] = max(
                        calculate_dp(i, j - 1) + piles[j], 
                        calculate_dp(i + 1, j) + piles[i])
            return dp[i][j]
            
            
        alex_cnt = calculate_dp(0, n-1)
        return alex_cnt > (cnt - alex_cnt)
        
        
# solution - dfs
class Solution:
    def stoneGame(self, piles) -> bool:
        #dfs with memory
        cnt_all = sum(piles)
        memory = dict()
        
        def dfs(cnt, start, end):
            if start > end:
                return 2 * cnt > cnt_all
            if start == end:
                return (cnt + piles[start]) * 2 > cnt_all
            if (cnt, start, end) not in memory.keys():
                memory[cnt, start, end] = dfs(cnt + piles[end], start, end - 1)  or dfs(cnt + piles[start], start + 1, end) 

            return memory[cnt, start, end]
        return dfs(0, 0, len(piles) - 1)
