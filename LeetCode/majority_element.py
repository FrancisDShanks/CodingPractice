class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return nums[0]
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
                if d[num] >= len(nums) / 2:
                    return num
            else:
                d[num] = 1
                
                
                
                
#another solution
#Boyer–Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        candidate = None
        for num in nums:
            if not count:
                candidate = num
            count += 1 if candidate == num else -1
        
        return candidate
        
