# Author - Francis Du
# 03/10/2016
#nothing concern

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        for i in range(0,len(nums)-1):
            if i%2 == 0:
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
                if nums[i]<nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]   
