# dp[i] 表示在第i个位置能再往后走的最远的可能
# dp[i] = max(dp[i-1]-1,nums[i]) 要么是nums[i],要么是i-1位置最远的可能减去一(走了一步到i)
# dp[0] = nums[0]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        if len(nums) == 1: return True
        
        n = len(nums)
        
        dp0 = nums[0]
        for i in range(1, len(nums)):
            if dp0 == 0:
                return False
            dp1 = max(dp0 - 1, nums[i])
            
            if len(nums) - 1 == dp1 + i:
                return True
            dp0 = dp1
        return True
