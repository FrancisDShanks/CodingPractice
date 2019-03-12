class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	#算法就是把每一个递增区间求一个profit,加起来就是总的profit
        if not prices or len(prices)<2:
            return 0
        res = 0
        cnt = 1
        while cnt < len(prices):
            small,large = prices[cnt-1],0
            while cnt<len(prices) and prices[cnt]<=prices[cnt-1]:
                small = min(small,prices[cnt])
                cnt += 1
            while cnt<len(prices) and prices[cnt]>=prices[cnt-1]:
                large = max(large,prices[cnt])
                cnt += 1       
            if large - small > 0:
                res += (large - small)
            
        return res
        