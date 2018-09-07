class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # 1. first put all words in a set(or dict)
        # 2. check each word, search for all it's postfix in the set,
        #    delete if the postfix is found in the set
        # 3. result = (length of set s) + (sum of length of each word remains in the set)
        
        s = set()
        for w in words:
            s.add(w)
        for w in words:
            if w not in s:
                continue
            for i in range(1,len(w)):
                if w[i:] in s:
                    s.remove(w[i:])
        
        res = len(s)
        for i in s:
            res += len(i)
        return res
