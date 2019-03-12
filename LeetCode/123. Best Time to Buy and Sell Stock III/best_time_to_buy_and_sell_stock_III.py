class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	# 算法:
	# 最多只能交易两次而且两次交易不能重叠也就是最多同时持有一个股,所以两次交易肯定是分布在两个不重叠的区间中
	# 设p[i] 为 分别在[0,i]和[i,n]两个区间获得的最大profit
	# 所以问题可以分解成在[0,n]区间里面,求max(p[0],...,p[n-1]),这里dp[0]是只交易一次的情况
	# p[i] = profit[0,i]+profit[i,n]
	# profit[0,i]就是best time to buy and sell stock I 里面的问题,正向DP一次可以求出
	# profit[i,n]类似于profit[0,i],反过来DP就可以求出
	# 求出profit[0,i]和profit[i,n]之后再求max(p[0],...,p[n-1])得出结果,这里把这一步和反向DP放在一次遍历完成
	# 此外,这题可以看做是best time to buy and sell stock IV的k=2的特殊情况,用IV的算法k=2也可以解题
        length = len(prices)
        if length <= 1:
            return 0
        
        small = prices[0]
        maxfromhead = [0 for _ in range(length)]
        for i in range(1,length):
            small = min(small,prices[i])
            maxfromhead[i] = max(maxfromhead[i-1],prices[i]-small)
            
        large = prices[-1]
        res = 0
        maxfromtail = 0
        for i in range(length-2,-1,-1):
            large = max(large,prices[i])
            maxfromtail = max(maxfromtail,large-prices[i])
            res = max(res,maxfromhead[i]+maxfromtail)
        return res