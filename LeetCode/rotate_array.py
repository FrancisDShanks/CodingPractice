class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if not k or k % len(nums) == 0:
            return
        for i in range(0,k % len(nums)):
            nums.insert(0,nums.pop(length - 1))
        return