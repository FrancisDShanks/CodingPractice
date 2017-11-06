'''
Created on Oct 22, 2014

@author: Xufan Du
@email: tctcdtc@gmail.com

'''

class Solution:
    # @return an integer
    # use the idea of sliding window
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        head = 0
        tail = 0
        res = 1
        while tail<len(s):
            if head == tail or s[tail] not in s[head:tail]:
                tail += 1
                res = max(res,tail-head)
            else:
                head +=1
        return res
