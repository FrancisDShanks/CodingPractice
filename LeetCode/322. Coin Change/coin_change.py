# DP 问题
# dp[i] = 1 if i == coin for coin in coins
# dp[i] = min(dp[i-coin]) + 1 for coin in coins and i > coin
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                elif i > coin:
                    if dp[i-coin] != -1:
                        if dp[i] == -1:
                            dp[i] = dp[i-coin] + 1 
                        else:
                            dp[i] = min(dp[i], dp[i-coin] + 1) 
        return dp[-1]
