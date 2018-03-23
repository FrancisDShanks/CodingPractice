# algorithm AC1 actually changes the size of nums
# this AC2 algorithm did not change the size of list
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        nlength = 0
        for index in range(length):
            if nums[index] != val:
                nums[nlength] = nums[index]
                nlength += 1

        return nlength