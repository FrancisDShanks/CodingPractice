class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        slen = len(strs[0])
        for i in range(1,len(strs)):
            if slen > len(strs[i]):
                slen = len(strs[i])
                
        if not slen:
            return ''
        
        ret = ''
        for i in range(0,slen):
            same = True
            for j in range(1,len(strs)):
                if strs[j][i] != strs[0][i]:
                    same = False
                    break
            if same:
                ret += strs[0][i]
            else:
                break
        return ret
                    
