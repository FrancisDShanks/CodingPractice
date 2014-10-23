# -*- coding: utf-8 -*-
'''
Created on Oct 23, 2014

@author: Xufan Du
@email: tctcdtc@gmail.com

'''


class Solution:
    # @param s, a string
    # @return an integer
    # Algorithm:
    #   Since we need to find the best solution, dp should be a good choice
    #   The DP function should be d[i] = min(d[i],d[j+1]+1]
    #       where i<=j<size, and s[i:j+1] is a palindrome partition, d[i] is min partitions of s[i:size]
    #       because s[i:j+1] is a palindrome partition, so s[i:size] can be part as s[i:j+1] and s[j+1:size]
    #       so d[i] = d[j+1]+1 (s[j+1:size]+s[i:j+1])
    #   
    #   -----------------------------------------------------------
    #   The way to check if a string is palindrome is also a dp function
    #   p[i][j] is True iff s[i]==s[j] && (p[i+1][j-1] || j-i<2)
    def minCut(self, s):
        size = len(s)
        #The one should pay attention is: we need give value to d[size]
        d = [size-i-1 for i in range(0,size+1)]
        p = [[False for i in range(0,size)] for j in range(0,size)]
        
        for i in range(size-1,-1,-1):
            for j in range(i,size):
                
                if s[i]==s[j] and (j-i<2 or p[i+1][j-1]):
                    d[i] = min(d[i],d[j+1]+1)
                    p[i][j]=True
        return d[0]
