# -*- coding: utf-8 -*-
'''
Created on Feb 26, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''
class Solution
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num)
        d={}
        if len(num) == 0
            return 0
        #put all the list into a dict, in order to reduce the access time
        for i in num
            d[i]=0
        max = 0
        #loop until go through all elements
        while d.keys()!=[]
            i=d.keys()[0]
            count=1
            t=i
            #delete the elements visited
            d.pop(t)
            #check left and right, after these two while, a Consecutive Sequence should be wiped out
            while d.has_key(t+1)
                #delete the elements visited
                d.pop(t+1)
                count+=1
                t=t+1
            t=i
            while d.has_key(t-1)
                #delete the elements visited
                d.pop(t-1)
                count+=1
                t=t-1
            if countmax max=count
        return max
