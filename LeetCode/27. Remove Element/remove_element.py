# replace the hit position with the num from the last position
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        while index < length:
            if nums[index] != val:
                index += 1
                continue
            # if this is the last number
            if index == length - 1:
                nums.pop()
            else:
                nums[index] = nums.pop()
            length = length - 1
        return length