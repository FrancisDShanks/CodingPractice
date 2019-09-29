# DP解法
# dp[i]表示N为i时Alice的输赢情况
# 对于0<k<i且i%k==0, Alice必赢,意味着所有的k里面存在 一种 k使得dp[i-k]为False. 也就是alice选这个k,bob必输
# 而如果所有的dp[i-k]都为True,则alice不管怎么选,Bob都必赢,所以alice必输
# 初始情况是dp[1]=False,dp[2]=True
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        ret = [False for _ in range(N + 1)]
        ret[2] = True
        for i in range(3, N + 1):
            for j in range(1, i):
                if i % j == 0 and not ret[i - j]:
                    ret[i] = True
        return ret[-1]
        
        
        
# 数学解法
# 1. 奇数的因子必定为奇数
# 2. 奇数减奇数必定为偶数
# 3. 由1,2可知奇数减自己的因子结果必定为偶数
# 4. 很容易推出游戏结束的条件为n=2 
# 5. 如果N为偶数,两种情况
#   1) N为2, alice赢
#   2) N>2, N必定有奇数因子(至少有一个1*N=N), alice取这个奇数因子,由推论3,bob下一次只能再取一个奇数因子,alice又得到一个偶数,回到5
# 所以最终只要N为偶数,alice必赢
# 6.如果N为奇数,由3,bob一定得到一个偶数,由5,bob必赢,alice必输
# 所以结果就是return N%2==0
class Solution:
    def divisorGame(self, N: int) -> bool:
        return   not (N % 2)
