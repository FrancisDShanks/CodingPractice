class Solution:
    # dp[n] = max(dp[n-2]+nums[n],dp[n-1])
    # dp[0] = nums[0]
    # dp[1] = max(nums[0],nums[1])
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp2, dp1 = max(dp1 + nums[i], dp2), dp2
        return dp2
        
            
        
