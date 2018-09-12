# using re lib
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s[::-1] == s
        
# using string methods
class Solution:
    def isPalindrome(self, s):
        s= [i.lower() for i in s if i.isalnum()]
        return s == s[::-1]
        # or 
        # return s[:len(s)/2] == s[(len(s)+1)/2:][::-1]
