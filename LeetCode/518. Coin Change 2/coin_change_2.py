# 1. dp[i][j] 表示由前i个coin组成amount为j的种类
# 2. dp[i-1][j] 表示由前i-1个组成j. 或者说由前i个组成j,且一个i都没有用到
# 3. dp[i][j-coins[i-1]] 表示由前i个组成j,且至少有一个i. 这里j-coin[i-1]就是有一个i之后剩的j
# 可以看到,2和3是互斥的, 1=2+3
# 当然如果j<coins[i-1]的情况2就是0,不可能发生
# 而当j=coins[i-1] 也就是dp[i][0]的情况,意味着由前i个组成j,且有一个i,剩下的j是0.也就是正好一个i就够了
# 所以所有的dp[i][0] = 1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        
        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                tmp = dp[i][j - coins[i-1]] if j >= coins[i-1] else 0
                dp[i][j] = dp[i-1][j] + tmp
                
        return dp[-1][-1]
    
    
# 还有更快的解法是把二维dp改成一维dp
#for coin in coins:
#    for i in range(len(dp)):
#        dp[i] = dp[i - coin]
