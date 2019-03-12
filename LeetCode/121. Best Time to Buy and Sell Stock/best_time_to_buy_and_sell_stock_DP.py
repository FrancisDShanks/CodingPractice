class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP solution: max_profit[n] = max(max_profit[n-1],prices[n]-smallest_in_n-1) when n>0
        #                            = 0 when n = 0
        res = 0
        if not prices or len(prices)<2:
            return res
        small = prices[0]
        for p in prices:
            small = min(small,p)
            res = max(res,p-small)
        return res
        
        