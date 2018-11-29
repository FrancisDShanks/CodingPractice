# two implementation
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l<1:return 0
        valid = 0
        i = 1
        while i < l:
            if nums[i] != nums[i-1]:
                valid += 1
                nums[valid] = nums[i]         
            i += 1
        return valid + 1
        
        
        
        
        
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        valid = 0
        i = 0
        while i < l:
            while i < l-1 and nums[i] == nums[i+1]:
                i += 1
            
            nums[valid] = nums[i]
            valid += 1
            i += 1
        return valid
