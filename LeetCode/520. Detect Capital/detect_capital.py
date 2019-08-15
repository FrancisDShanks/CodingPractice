class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.lower() or word == word.upper() or word == word.capitalize()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper() and word[1:].islower():
            return True
        elif word.isupper() or word.islower():
            return True
        else:
            return False
