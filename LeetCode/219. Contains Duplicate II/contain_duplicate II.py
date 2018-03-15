# use dict(hash-table)
# notice if there are more than three num are equal
# 1,...,i,...,j,...,k,...
# where nums[i] = nums[j] = nums[n]
# if j-i<k then return True
# if j-i>k, then n-i > j-i >k, so there is no need to record i
# aka. the hash table only need to record the last appearance of the duplicate number

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for j in range(0, len(nums)):
            if nums[j] in d.keys():
                i = d[nums[j]]
                if j - i <= k:
                    return True
            d[nums[j]] = j
        return False
