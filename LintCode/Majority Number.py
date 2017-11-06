#Majority Number
#02-29-2016
#

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        d = {}
        for i in range(0,len(nums)):
            if not d.has_key(nums[i]):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        max = 0
        res = 0
        for k in d.keys():
            if max < d[k]:
                max = d[k]
                res = k
        return res
            
#challenge time:O(n)   space:O(1)
#mistake:
#       see comments
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        cnt = 0
        maj = 0
        for i in range(0,len(nums)):
            if nums[i] != maj:
                if cnt == 0:
                    maj = nums[i]
                    cnt = 1 //made mistake here, missed this line, so failed on [1,2,1,2,1,2,1,2,2]
                else:
                    cnt -= 1
            else:
                cnt += 1
        
        if cnt>0:
            chk = 0
            for i in range(0,len(nums)):
                if nums[i] == maj:
                    chk += 1
            if chk > len(nums) / 2:
                return maj
        return 
