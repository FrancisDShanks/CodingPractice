# classical binary search problem
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = len(nums)
        left = 0
        right = l - 1
        while left <= right:
            
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                return mid
            # notice here shoule be '<=', because when there two elements left eg. find 1 in [3,1]
            # [left,mid] is [3] which shoule be treated as a increasing interval.
            # if it is '<' here and try to find 1 in [3,1] it will return -1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return -1
