# straight forward problem
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l = list()
        for word in words:
            m_index = [ord(letter)-97 for letter in word]
            m_code = [morse[i] for i in m_index]
            res = ''.join(m_code)
            if res not in l:
                l.append(res)
        return len(l)