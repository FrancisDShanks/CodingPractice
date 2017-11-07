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
    
    
    #three time reverse solution
    class Solution:
    #helper to reverse a list nums from start to end in place
    def reverse(self, nums, start, end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        if not k:
            return
        self.reverse(nums, 0, length - k - 1)
        self.reverse(nums, length - k, length - 1)
        self.reverse(nums, 0, length - 1)
        return
