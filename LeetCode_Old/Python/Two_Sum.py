# -*- coding: utf-8 -*-
'''
Created on Feb 07, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num)<2:
            return 'List too short'
        for i in range(0,len(num)):
            num[i] = (i+1,num[i])
        num = sorted(num,key=lambda num: num[1])
        left = 0 
        right = len(num)-1
        while(left<right):
            if num[left][1]+num[right][1] == target:
                return (num[left][0],num[right][0]) if num[left][0]<num[right][0] else (num[right][0],num[left][0])
            elif num[left][1]+num[right][1] > target:
                right -= 1
            else:
                left += 1
        return 'Not Found'
        
    
if __name__ == '__main__':
    s = Solution()
    num = [2,7,11,15]
    print s.twoSum(num,9)

#hash 方法
#暴力搜索法
