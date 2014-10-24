# -*- coding: utf-8 -*-
'''
Created on Oct 24, 2014

@author: Xufan Du
@email: tctcdtc@gmail.com

'''
class Solution:
    # @return a boolean
    # 二叉树 一定要考虑递归方法能不能用，这题就很适合
    # 递归之前一系列筛选减少很多运算
    def isScramble(self, s1, s2):
        if s1==s2: return True
        if len(s1)!=len(s2): return False
        tmps1 = list(s1)
        tmps2 = list(s2)
        tmps1.sort()
        tmps2.sort()
        if tmps1!=tmps2: return False
        
                
        
        for i in xrange(1,len(s1)):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[len(s2)-i:]) and self.isScramble(s1[i:],s2[:len(s2)-i]):
                return True
        return False
