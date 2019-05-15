class Solution:
    def binaryGap(self, N: int) -> int:
        s = str(bin(N))[2:]  #生成对应二进制字符串
        index = [i for i in range(len(s)) if s[i]=='1']  #生成包含s中所有为'1'的字符的下标的list
        if len(index)>1:
            j = [(index[j+1] - index[j]) for j in range(len(index)-1)]  #j是index中相邻两个指标的差值
            return max(j)
        else:
            return 0
