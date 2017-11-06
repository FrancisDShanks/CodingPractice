# -*- coding: utf-8 -*-
'''
Created on March 24, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''
class Solution:
    # @return a string
    def intToRoman(self, num):
        rad=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        roman=""
        index=-1
        while num>0:
            index+=1
            count=num/rad[index]
            num=num%rad[index]
            for i in range(0,count):
                roman+=sym[index]
        return roman
