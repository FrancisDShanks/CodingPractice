# quick-sort implementation
# 这种实现每次是交换high和low
class Solution(object):
    def run_qsort(self, nums):
        self.qsort(nums, 0, len(nums) - 1)
        return nums
    
    def qsort(self, nums, start, end):
        if start >= end:
            return
        p = nums[end]

        low = start
        high = end
        while low < high:
            while nums[low] < p and low < high:
                low += 1
            if low < high:
                nums[high],nums[low] = nums[low],nums[high]

            
            while p <= nums[high] and low < high:
                high -= 1
            if low < high:
                nums[high],nums[low] = nums[low],nums[high]

                               
        self.qsort(nums, start, low - 1)
        self.qsort(nums, low + 1, end)
        return
        
# quick-sort implementation   
# 这种实现是实现了教材里面的快排
# 需要注意的是每次交换是覆盖的
class Solution(object):
    def run_qsort(self, nums):
        self.qsort(nums, 0, len(nums) - 1)
        return nums
    
    def qsort(self, nums, start, end):
        if start >= end:
            return
        
        p = nums[end]
        low = start
        high = end
        
        while low < high:
            while nums[low] < p and low < high:
                low += 1
            if low < high:
                nums[high] = nums[low]
            
            while p <= nums[high] and low < high:
                high -= 1
            if low < high:
                nums[low] = nums[high]
                
        nums[low] = p                
        self.qsort(nums, start, low - 1)
        self.qsort(nums, low + 1, end)
        return
