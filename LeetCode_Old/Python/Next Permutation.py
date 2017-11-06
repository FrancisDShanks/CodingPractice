 # -*- coding: utf-8 -*-
'''
Created on Oct 17, 2014

@author: Francis Xufan Du
@email: tctcdtc@gmail.com
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    #The algorithm is()from wikipedia.org:
    #1.Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    #2.Find the largest index l greater than k such that a[k] < a[l].
    #3.Swap the value of a[k] with that of a[l].
    #4.Reverse the sequence from a[k + 1] up to and including the final element a[n].
    def nextPermutation(self, num):
        index = len(num)-2
        while index>=0:
            if num[index]<num[index+1]:
                break
            index -= 1
        if index<0:
            num.reverse()
            return num
        ind = len(num)-1
        while ind>0:
            if num[ind]>num[index]:
                break
            ind -= 1
        num[ind],num[index] = num[index],num[ind]
        tmp = num[index+1:]
        tmp.reverse()
        num=num[0:index+1] + tmp
        return num
