# bitmapping solution is faster 
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        size = 2**len(nums)
        for i in range(size):
            tmp = i
            v = []
            for j in range(len(nums)):
                if tmp % 2 == 1:
                    v.append(nums[j])
                tmp //= 2
            res.append(v)
        return res
