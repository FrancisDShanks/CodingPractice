class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = len(nums)
        left = 0
        right = l - 1
        while left <= right: 
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                return True
            
            elif nums[left] <= nums[mid]:
                while(left < mid and nums[left] == nums[mid]):
                    mid -= 1
                # 注意这里要再次判断,这里的mid和前面的mid不一样了,不判断之后mid-1或mid+1后会漏掉mid
                if nums[mid] == target: return True
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                
                while(mid < right and nums[mid] == nums[right]):
                    mid += 1
                # 注意这里要再次判断,这里的mid和前面的mid不一样了,不判断之后mid-1或mid+1后会漏掉mid
                if nums[mid] == target: return True
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return False
