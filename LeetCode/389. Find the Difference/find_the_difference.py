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
                
             
#using XOR (much better/faster one)
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        length = len(t)
        xor = ord(t[length - 1])
        for i in range(0,length-1):
            xor ^= ord(s[i]) 
            xor ^= ord(t[i])
        return chr(xor)
        
