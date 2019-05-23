# solution 1, basic binary search like solution
class Solution(object):
    # since nums[-1] and nums[n] are smallest number
    # compare nums[mid] and nums[mid+1]
    # if nums[mid] > nums[mid+1], then there must be a peak in (-1:mid)
    # else there must be a peak in (mid+1,n)
    # similar idea with binary search
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums) - 1
        while True:            
            mid = left + (right - left) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
            elif mid==len(nums)-1:
                if nums[mid] > nums[mid - 1]:
                    return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

# solution 2, add -infinite to nums
class Solution(object):
    # since nums[-1] and nums[n] are smallest number
    # compare nums[mid] and nums[mid+1]
    # if nums[mid] > nums[mid+1], then there must be a peak in (-1:mid)
    # else there must be a peak in (mid+1,n)
    # similar idea with binary search
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums.insert(0,-sys.maxsize)
        nums.append(-sys.maxsize)
        
        left = 1
        right = len(nums) - 2
        while True:            
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
                
 
 # solution 3, solution converts from solution 1        
 class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] < nums[right] else right
