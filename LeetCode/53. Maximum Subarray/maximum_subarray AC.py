# time complexity is O(n)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max sum of the sub-array contains the current num
        # note that for num i, if max_sum_contain_current for (i-1) is smaller than 0
        # then max_so_far for i should be i > i + max_sum_contain_current for (i-1)
        max_sum_contain_current = 0
        # current maximum result
        max_result = -sys.maxsize
        for index in range(0, len(nums)):
            if max_sum_contain_current <= 0:
                max_sum_contain_current = nums[index]
            else:
                max_sum_contain_current += nums[index]
            max_result = max(max_result, max_sum_contain_current)
        return max_result