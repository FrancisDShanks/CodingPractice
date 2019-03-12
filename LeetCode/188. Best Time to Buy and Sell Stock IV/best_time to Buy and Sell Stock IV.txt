class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
	#算法:
	# 定义一个局部最优解local[i][j],为第i天进行j次交易,且最后一次交易是i天当天卖出的最优解
	# 定义一个全局最优解globl[i][j],为第i天进行j次交易的最大收益
	# globl[i][j]的递归公式比较直观
	# globl[i][j] = 0 if j=0
	# globl[i][j] = max(globl[i-1][j],local[i][j]) if j>0
	# 解释是第i天进行j次交易的最优解有两种情况,分为第i天当天交易或者不交易
	# 第一种情况i天当天交易,globl[i][j]=local[i][j]
	# 第二种情况i天当天不进行任何交易,globl[i][j]=globl[i-1][j]
	#
	# local[i][j] 的递归公式为
	# local[i][j] = 0 if j=0
	# local[i][j] = max(globl[i-1][j-1]+diff,local[i-1][j]+diff) if j>0
	# 这里diff=prices[i] - prices[i-1], i天当天价格和前一天价格的差值
	# 解释如下:
	# 第i天的局部最优解也分两种情况,i天当天肯定交易了且是卖出,那么卖出的股票分为是前一天买入的或是更早之前买入的
	# 第一种情况卖出的股票是前一天买入的,local[i][j] = globl[i-1][j-1]+diff, 是i-1天j-1次交易的全局最优解加上i-1天买i天卖赚的diff,注意diff可能是负值
	# 第二种情况卖出的股票分是更早之前买入的,那么local[i][j] = local[i-1][j]+diff, 
	# local[i-1][j]是i-1天j次交易的局部最优解,且在i-1天卖出的情况
	# 那么local[i][j]就是i-1天不卖留到i天卖,就是local[i][j] = local[i-1][j]+diff,这里diff也可能是负值
	#注意点:
	# 开始用的二维数组写递归,后来发现递归公式只需要用到i-1和j-1的数据,所以可以用两个一维数组代替二维数组,节省内存
	# 后来提交还是TLE,注意到TLE的情况是k远大于len(prices)的情况
	# 可以分析当k>len(prices)时,就相当于在len(prices)天内可以做最大次交易(因为一天最多一次),最大交易次数为len(prices)
	# 这就相当于 best time to sell and sold stock II 的问题,所以做个判断这种情况用II的算法,其他情况用双DP做
        length = len(prices)
        if length <= 1 or k < 1:
            return 0
        
        # if k is larger than length(prices), the question is the with Best Time II
        # in this case, using DP may cost a lot of memory resource if k is really large
        # so use the algorithm from Best Time II when k>length
        if k>=length:
            cnt = 1
            res = 0
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
            
        
        local_prev = [0 for _ in range(k+1)]
        globl_prev = [0 for _ in range(k+1)]
        local = [0 for _ in range(k+1)]
        globl = [0 for _ in range(k+1)]
        for i in range(1,length):
            diff = prices[i] - prices[i-1]
            for j in range(1,k+1):
                local[j] = max(globl_prev[j-1] + diff,local_prev[j] + diff)
                globl[j] = max(local[j],globl_prev[j])
                
                local_prev[j-1] = local[j-1]
                globl_prev[j-1] = globl[j-1]
            local_prev[k] = local[k]
            globl_prev[k] = globl[k]
            
            
                
        return globl[k]