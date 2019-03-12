class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	#分别判断递增递减区间的算法
        if not prices or len(prices)<2:
            return 0
        res,small = 0,0
        cnt = 1
        while cnt < len(prices):
            small = prices[cnt-1]
            while cnt<len(prices) and prices[cnt]<=prices[cnt-1]:
                small = min(small,prices[cnt])
                cnt += 1
            while cnt<len(prices) and prices[cnt]>=small:
                res = max(res,prices[cnt]-small)
                cnt += 1       
            
        return max(res,prices[-1]-small)