class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. use a dict to count appearance of each characters
        #    key is the letter, dict[key] is the count
        # 2. sort based on dict value
        # 3. construct the result with letter and it's count, key*dict[key]
        d = dict()
        for letter in s:
            d[letter] = d[letter] + 1 if letter in d.keys() else 1
        
        t = sorted(d.items(),key=lambda x:x[1],reverse=True)
        res = ''
        for i in t:
            res = ''.join([res,i[0]*i[1]])
        return res
