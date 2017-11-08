#using hash table    
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for char in s:
            dic[char] = dic[char] + 1 if char in dic else 1
        for char in t:
            if char in dic and dic[char] >= 1:
                dic[char] -= 1
            else:
                return char
                
             
