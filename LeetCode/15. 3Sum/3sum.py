class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for index1 in range(0,len(nums)-2):
            # remove duplicates
            if index1>0 and nums[index1]==nums[index1-1]:
                continue
            target = 0 - nums[index1]
            index2 = index1 + 1
            index3 = len(nums) - 1
            while index2 < index3:
                if nums[index2] + nums[index3] == target:
                    res.append([nums[index1],nums[index2],nums[index3]])
                    index2 += 1
                    index3 -= 1
                    while index2<index3:
                        if nums[index2]==nums[index2-1]:
                            index2+=1
                        else:
                            break
                    while index2<index3:
                        if nums[index3]==nums[index3+1]:
                            index3-=1
                        else:
                            break                
                elif nums[index2] + nums[index3] < target:
                    index2 += 1
                else:
                    index3 -= 1
        return res
