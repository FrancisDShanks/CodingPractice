# this problem can be solved with dp
# draw a matrix of A and B, then it can be easily found that:
# let dp[i][j] be the length of subarray of A(0~i) B(0~j)
# if A[i]==B[j], then dp[i][j] = dp[i-1][j-1] + 1
# modified to use a one-dimensional array to save memory cost
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [0 for _ in range(len(B)+1)]
        pre = [0 for _ in range(len(B)+1)]
        ret = 0
        for i in range(0, len(A)):
            for j in range(1, len(B) + 1):
                if A[i] == B[j - 1]:
                    # 这里有个bug, 一开始用的j是range(0,len(B))
                    # 当A[i]==B[j],j=0的时候, dp[j]=pre[j-1]
                    # 因为python的list的特性, 这里就会取pre[-1]的值取到pre的最后一个值去了
                    # 所以我让dp和pre长度为range(0,len(B)+1), j取值为range(1,len(B)+1)
                    # 前面放一个0来防止bug发生
                    dp[j] = pre[j - 1] + 1
                else:
                    dp[j] = 0
            ret = max(ret, max(dp))
            dp, pre = pre, dp
        return ret
