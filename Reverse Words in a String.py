# -*- coding: utf-8 -*-
'''
Created on March 11, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if s=="":
            return s
        index=0
        while(index<len(s)):
            if s[index] != ' ':
                break
            index+=1
        if index==len(s):
            return ''
        
        l=''
        al=[]
        while(index<len(s)):
            if s[index]==' ' and s[index-1]!=' ':
                al.append(l)
                l=''
            elif s[index]!=' ':
                l+=s[index]
            index+=1
        if l!='':
            al.append(l)
        res=''
        
        
        for i in range(len(al)-1,0,-1):
            res+=al[i]
            res+=' '
        res+=al[0]

        return res
            
