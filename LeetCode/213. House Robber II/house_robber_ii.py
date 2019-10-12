# 最后去的house的结果,不可能既有第一个又有最后一个
# 所以没有第一个和没有最后一个两种情况覆盖了所有情况(包括两者都没有)
# 所以跑两次dp,求两者的最大值,一次nums[:-1]再跑一次nums[1:]
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
class Solution:
    def run_dp(self, nums):
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1]) # 这里容易出错
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp[-1], dp[-2])
        
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        
        return max(self.run_dp(nums[1:]), self.run_dp(nums[:-1]))
        
# 优化:可以不用保存整个dp数组,只保存最近的连个位置就行了
class Solution:
    def run_dp(self, nums):
            dp = [nums[0], max(nums[0], nums[1])]
            for i in range(2, len(nums)):
                dp[i%2] = max(dp[(i-1)%2], dp[(i-2)%2] + nums[i])
            return max(dp)
        
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        
        return max(self.run_dp(nums[1:]), self.run_dp(nums[:-1]))
        
