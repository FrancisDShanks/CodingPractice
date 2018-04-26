class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = dict()
        for i in range(0,len(nums)):
            d[nums[i]] = i
        keys = list(d.keys())
        keys.sort()
        keys = keys[::-1]
        res = ['' for i in range(0,len(nums))]
        rank = "Gold Medal"
        cnt = 1
        for k in keys:
            res[d[k]] = rank
            cnt += 1
            if rank=="Gold Medal":
                rank="Silver Medal"
            elif rank=="Silver Medal":
                rank="Bronze Medal"
            else:
                rank = str(cnt)
            
        return res
