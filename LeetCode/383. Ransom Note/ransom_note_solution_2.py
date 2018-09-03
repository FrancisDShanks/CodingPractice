class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # lookup list
        l = [0 for _ in range(26)]
        
        # ord('a') = 97
        for letter in magazine:
            l[ord(letter) - 97] += 1
        
        for letter in ransomNote:
            index = ord(letter) - 97
            if l[index] < 1:
                return False
            l[index] -= 1
        return True
