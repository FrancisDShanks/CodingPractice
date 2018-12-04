class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right: 
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                return True
            # 因为有重复的数字,所以[1,1,1,1,3,1,1,1]这种情况就不知道在mid左还是右,就直接left+=1,再继续计算
            elif nums[left] == nums[mid] : 
                left += 1
            elif nums[left] < nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return False
