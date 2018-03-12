#using XOR operation
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = nums[len(nums)-1]
        for i in range(0,len(nums)-1):
            xor ^= nums[i]
        return xor
