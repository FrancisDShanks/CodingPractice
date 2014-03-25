# -*- coding: utf-8 -*-
'''
Created on March 24, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        sym1=["M","D","C","L","X","V","I"]
        sym2=["CM","CD","XC","XL","IX","IV"]
        rad1=[1000,500,100,50,10,5,1]
        rad2=[900,400,90,40,9,4]
        index = len(s)-1
        index1 = 6
        index2 = 5
        res = 0
        while index>=0:
            if index1>=0:
                while s[index]==sym1[index1] and index>=0:
                    index-=1
                    res+=rad1[index1]
            if index2>=0:
                while s[index-1:index+1]==sym2[index2] and index>=0:
                    index-=2
                    res+=rad2[index2]
            index1-=1
            index2-=1
        
        return res
