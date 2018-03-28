class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d.keys():
                return [d[nums[i]], i]
            d[target - nums[i]] = i
        return []