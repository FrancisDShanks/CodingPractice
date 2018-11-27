# a little modify based on the solution of Subsets I
class Solution:
    def subsetsWithDup(self, nums):
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
            for j in range(0,len(nums)):
                if tmp%2==1:
                    v.append(nums[j])
                tmp //= 2
            if v not in res:
                res.append(v)
        return res
