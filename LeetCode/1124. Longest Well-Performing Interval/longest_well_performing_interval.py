class Solution:
    def longestWPI(self, hours):
        # record prefix sum(sum from 0 to i)
        pre = 0
        ret = 0
        shown = {}
        for i, h in enumerate(hours):
            pre = pre + 1 if h > 8 else pre - 1
            # if prefix of 0~i larger than 0, then 0~i as a whole is WPI
            # and it must larger than previous ret
            if pre > 0:
                ret = i + 1
            else:
                # if prefix < 0, the WPI of interval 0~i is either previous ret(previous shown possibility of WPI intervals)
                # or WPI of interval shown[pre - 1] ~ i(a new interval contains position i)
                # explain: 
                # because the prefix sum is always continous(because new pre = pre + 1 or -1)
                # so if pre shown before, then interval position shown[pre] ~ position i is a interval sum 0, 
                # 想象一个连续曲线,两个相同的y值意味着曲线一定由相同数量1和-1组成
                # so if (pre-1) shown before, than position shown[pre-1] ~ position i is a interval sum 1, which is a WPI
                
                shown.setdefault(pre, i)
                if pre - 1 in shown:
                    ret = max(ret, i - shown[pre - 1])
        return ret
                    
                
