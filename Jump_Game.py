# -*- coding: utf-8 -*-
'''
Created on Feb 10, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        #no element, cannot reach the 'last one'
        if len(A)==0: return False
        #if only one element, can reach the last one
        if len(A)==1: return True
        m=0
        for i in range(0,len(A)):
            if i<=m:
                m = m if m>(A[i]+i) else (A[i]+i)
            if m>=len(A)-1:
                return True
        return False

