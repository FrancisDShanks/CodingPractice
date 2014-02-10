# -*- coding: utf-8 -*-
'''
Created on Feb 09, 2014

@author: Xufan Du, tctcdtc@gmail.com

'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        if s=='' :return False
        index = 0
        while index<len(s) and s[index]==' ':
            index+=1
            
        if index<len(s):
            if s[index]=='+' or s[index]=='-':
                index+=1
            
        dotshown = False
        eshown = False
        spaceshown = False
        #if has 'e', before 'e' is part1 and after 'e' is part two
        part = 0
        while(index<len(s)):
            if s[index] == '.':
                if spaceshown: return False
                if dotshown or eshown:
                    return False
                dotshown = True
            elif s[index] =='e' or s[index] == 'E':
                if spaceshown: return False
                if eshown:
                    return False
                if part==0:
                    return False
                eshown = True
                
            elif s[index] == '+' or s[index] == '-':
                if spaceshown: return False
                if eshown==False:
                    return False
                if s[index-1]!='e' and s[index-1]!='E':
                    return False
            elif s[index].isdigit():
                if spaceshown: return False
                if eshown:
                    part=2
                else:
                    part=1
            elif s[index]==' ':
                spaceshown = True
            else:
                return False
            index+=1
        
        if part==0:
            return False
        if eshown and part==1:
            return False
        return True
                
    
if __name__ == '__main__':
    s = Solution()
    str=''
    while str!='0-0-0':
        str=raw_input()
        print s.isNumber(str)
