# compare maxSubArray(nums[1:]) and maxArray(start from nums[0])
# My error: return m if m and max_contain_current < m else max_contain_current
# I want to check if m is None or not, but when m = 0, it is not None but it is false in if statement!
# TLE , time complexity is O(n^2)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        max_contain_current = nums[0]
        current_sum = nums[0]
        for index in range(1, len(nums)):
            current_sum += nums[index]
            if current_sum > max_contain_current:
                max_contain_current = current_sum
        m = self.maxSubArray(nums[1:])
        return m if m is not None and max_contain_current < m else max_contain_current