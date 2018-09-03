class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # construct a dict to count all letters' appears in magazine
        # search each letter in ransomNote in the dict
        # if the letter is not in dict, return false
        # if the letter is in the dict, the count -1 means one letter has been used
        # when the count = 0, delete the ket means the letter has been used out
        # O(n,m) = n + m
        d = dict()
        for letter in magazine:
            if letter in d.keys():
                d[letter] += 1
            else:
                d[letter] = 1
        
        for letter in ransomNote:
            if letter not in d.keys():
                return False
            else:
                d[letter] -= 1
                if d[letter] == 0:
                    d.pop(letter)
        return True
        
        # another fast algorithm thought:
        # there are 26 letters(ignore case), so just build a 26keys dict to do this.
