# solution - 1 : find the specific location
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0 or target < nums[0]:
            return 0
        if target > nums[right]:
            return right + 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid - 1] < target < nums[mid]:
                return mid
            elif nums[mid] < target < nums[mid + 1]:
                return mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
 
 
 # solution - 2 : find the first element larger than target
 # than the element is the place to insert target
 class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0 or target < nums[0]:
            return 0
        if target > nums[right]:
            return right + 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left + (right - left) // 2 + 1
