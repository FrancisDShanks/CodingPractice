# -*- coding: utf-8 -*-
'''
Created on April 15, 2014

@author: Francis Xufan Du
@email: tctcdtc@gmail.com

'''
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res = []
        self.recursion(mapping,0,"",digits,res)
        return res
        
        
    def recursion(self,mapping,index,curstr,digits,res):
        if index>=len(digits):
            res.append(curstr)
            return
        
        #ASCII code of '1' is 49
        curdig = ord(digits[index])-48
        if curdig>0 and curdig<10:
            for i in range(0,len(mapping[curdig])):
                self.recursion(mapping,index+1,curstr+mapping[curdig][i],digits,res)
        return
