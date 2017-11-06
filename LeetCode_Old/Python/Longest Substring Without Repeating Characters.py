# -*- coding: utf-8 -*-
'''
Created on March 06, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        #use dict to check if repeating
        dic={}
        #longth of a substring
        sum=0
        #longth of longest one
        m=0
        i=0
        while i<len(s):
            #if repeating
            if dic.has_key(s[i]):
                #back index to where the repeat happens
                i=dic[s[i]]
                #clean the dic
                dic={}
                m=max(m,sum)
                sum=0
            else:
                #put the non-repeating char as key of dict
                #the position as value of dict
                dic[s[i]]=i
                sum+=1
            i+=1
        
        m=max(m,sum)
        return m
