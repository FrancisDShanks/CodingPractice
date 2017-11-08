#using XOR operation
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = len(nums)
        for i in range(0,len(nums)):
            xor ^= i
            xor ^= nums[i]
        return xor
        
