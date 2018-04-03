# This is a math problem
# think about 1 step : n-1 numbers add 1
# this step makes the distance from the max_number to other numbers reduce one(the distance can be -1)
# so we can change a way to think about this, a step to make n-1 numbers add 1 equals to make the max_number minus 1
# it also makes the distance from the max_number to other numbers reduce one
# the question changes to "how many steps needed to make all numbers equals to the min_number,
# where each step is make the max_number -1
# so easy to get
# steps = (nums[0] - min_num) + (nums[1] - min_num) + ... + (nums[n-1] - min_num)
# final result = sum(nums) - n * min_num


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)