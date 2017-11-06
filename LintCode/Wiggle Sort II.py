# Author - Francis Du
# 03/10/2016

#this is easy way
# Time - O(nlgn)     sorting takes O(nlgn)
# Space - O(n)
class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        l = len(nums)
        snums = sorted(nums)
        for i in range(1,l,2)+range(0,l,2):
            nums[i] = snums.pop()
            
            
# chanllege 
# Time - O(n)
# Space - O(1)
# 1. QuickSelect - O(n) - find the n/2 th lagest number in the list ( mid )
#                                                             f(n)
# 2. use a function to map nums to fnums, (0,1,2 ... ,n-1) ------------>  (0,2,4,....,1,3,....)
# 3. put nums[i]<mid to fnums[0,n/2], nums[i]>mid to fnums[n/2+1,n-1], for i =(0,1,2, ... ,n-1)
