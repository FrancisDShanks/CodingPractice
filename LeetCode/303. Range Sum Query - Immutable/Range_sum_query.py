# dynamic programming problem
# dp[i] represents sum of range from 0 to i
# the result sumRange(i,j) = dp[j] - dp[i - 1]
# be notice that when i=0, sumRange(i,j) = dp[j]
# at first I build a two-dimension dp and got a TLE ...
# don't build high dimensional dp if low dimensional dp is possible

class NumArray:
    def __init__(self, nums):
        self.dp = nums  #dp[i] represents sum of range from 0 to i
        
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]


    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.dp[j]
        return self.dp[j] - self.dp[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
