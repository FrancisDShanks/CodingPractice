class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # search from both side
        # 尽量做到了只扫一遍,考虑到一遍要找中位数,用了两个指针从两头往中间找
        # 最小值最大值就是两个指针分别遇到的第一个非0的数
        # 几下总的个数和总和,就可以得到平均值
        # 维护一个最大的count,就是众数
        # 中位数
        # 维护一个balance,左边处理一个数,balance加这个个数,balance为正表示左边多处理了
        # 右边处理一个数,balance减去这个个数,balance为负表示右边多处理了
        # 扫的时候,balance为正就动右边指针,为负就动左边指针
        # 扫完一遍后
        # balance为0表示正好终止的点左边右边一样多,那总数肯定是偶数个,左边最后处理的和右边最后处理的数两个是中位数
        # 为正表示左边多了,中位数是左边最后处理的数
        # 为负表示右边多了,中位数是右边最后处理的数
        i = 0
        j = len(count) - 1
        lasti, lastj = i, j
        
        add = 0 #总和,用来求平均值
        cnt = 0 #总个数,求平均值
        maxcnt = [0, 0] #最大的count,众数
        ret = [0] * 5
        checkmin = True 
        checkmax = True
        balance = 0
        
        
        while i <= j:
            # 跳过0
            while count[i] == 0:
                i += 1            
            while count[j] == 0:
                j -= 1                
            
            # 没找到最大值或最小值就找
            if checkmin:
                if count[i] > 0:
                    ret[0] = float(i)
                    checkmin = False
            
            if checkmax:
                if count[j] > 0:
                    ret[1] = float(j)
                    checkmax = False
                    
            # 根据balance值选择动哪个指针
            if balance <= 0:
                cnt += count[i]
                add += count[i] * i
                
                if count[i] > maxcnt[0]:
                    maxcnt = [count[i], i]
                
                balance += count[i]
                lasti = i
                i += 1
            else:
                cnt += count[j]
                add += count[j]  * j
                
                if count[j] > maxcnt[0]:
                    maxcnt = [count[j], j]
                    
                balance -= count[j]
                lastj = j
                j -= 1
                
        if balance == 0:
            ret[3] = float((lasti + lastj) / 2)
        elif balance > 0:
            ret[3] = float(lasti)
        else:
            ret[3] = float(lastj)
            
        ret[2] = float(add / cnt)
        ret[4] = float(maxcnt[1])
        return ret
