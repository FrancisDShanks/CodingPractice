# use two pointers from both sides
# one for 0 and one for 2
# go one pass through the list
# move all found 0s to left point and 2s to right point
# all remains in the middle are the 1s
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
                # notice here, because the loop is from left to right
                # so for 0s, swap i nums[i], nums[start] and start + 1 is enough
                # because nums[start] must has been looped before
                # but for nums[end], it has not been visited
                # so after swap nums[i] and nums[end]
                # nums[end] (which is new nums[i] should be visited
                # so i should go one step back
                i -= 1
            i += 1
        
            
