#using binary search
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            #notice here! have to check if start>end to make sure the left part can be cut off
            if nums[mid] > nums[start] and nums[start] > nums[end]:
                start = mid
            
            if nums[end] > nums[mid]:
                end = mid
                
        return min(nums[start], nums[end])
        
        
        
#a better solution using binary search        
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
                
        return nums[start]        
