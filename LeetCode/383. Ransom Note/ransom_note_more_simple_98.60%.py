class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # take advantage of set() and count()
        
        r = set(ransomNote)        
        for letter in r:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
