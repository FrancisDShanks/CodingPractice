# -*- coding: utf-8 -*-
'''
Created on Oct 24, 2014

@author: Xufan Du
@email: tctcdtc@gmail.com

'''

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    # Algorithm:
    #   a substring in S while is valid must:
    #       1.has a length of numOfWordsinL * lengthOfWordinL
    #       2.each word in L must appears just once in the substring once
    #   so just check all possible substrings in L, which is S[i:i+numOfWordsinL * lengthOfWordinL] 0<=i<len(S)-numOfWordsinL * lengthOfWordinL+1
    #   When check if all words in L appears once:
    #       I first use dict, but it got a Time Limit Exceeded error in Leetcode
    #       Then I learn from a blog that use a list is enough, split the substring based on the length of word, then check each word in L with the substring,
    #       If it is in the substring, just remove it from the substring
    #
    #   Time complexity: O(n*m) n is size of S, m is size of L. O((n-m*lengthofword)*m)
    #   Space complexity: O(m)
    def findSubstring(self, S, L):
        res = []
        nums = len(L)
        if nums==0: return res
        size = len(L[0])
        for i in xrange(len(S)-nums*size+1):
            tmp = [S[start:start+size] for start in xrange(i,i+nums*size,size)]
            found = True
            for item in L:
                if item in tmp:
                    tmp.remove(item)
                else:
                    found = False
                    break
            if found: res.append(i)
        return res
            
