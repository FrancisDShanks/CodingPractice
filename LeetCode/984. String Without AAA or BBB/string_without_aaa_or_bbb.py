class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        #分组的思路
        # 把A个'a'和B个'b'分组,最后接在一起
        #长度长的无脑两个两个一组,最后一组可能只剩一个
        #长度短的先保证组数,一组一个,多余的再每组补一个直到用完
        if A >= B:
            more = A
            moreletter = 'a'
            less = B
            lessletter = 'b'
        else:
            more = B
            moreletter = 'b'
            less = A
            lessletter = 'a'
            
        #groups 分组,组数根据长度长的算
        g = more // 2 + more % 2
        more_group = [moreletter * 2] * g
        if more % 2 == 1:
            more_group[-1] = moreletter
        
        # 短的组数要么等于长的组数,要么少1
        if less == g - 1:
            g = g - 1        
        
        # 先只放一个
        less_group = [lessletter] * g
        # 多余的再补
        cnt = 0
        while cnt < less - g:
            less_group[cnt] += lessletter
            cnt += 1
            
            
        # combine
        if len(less_group) < len(more_group):
            less_group.append('')
        res = map(lambda a,b:a+b,more_group,less_group)
        return ''.join(list(res))
