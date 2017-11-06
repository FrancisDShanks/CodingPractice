class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        #if the list if empty, common prefix will be ""
        if len(strs)==0: return ""
        
        #if there is an empty string, common prefix will be ""
        if strs[0]=="": return ""
        
        #s stores the first string, the common prefix must be part of s
        #stores length of current common prefix
        #so s[0:count+1] will be the current common prefix
        s = strs[0]
        count = len(s)-1
        
        #loop, go through the list
        for i in range(1,len(strs)):
            #temp is the length of same chars between s and current string
            temp=-1
            #loop, compare s with a string
            for j in range(0,count+1):
                #if there is an empty string, common prefix will be ""
                if strs[i]=="": return ""
                
                #if the string is shorter than s, break
                if len(strs[i])==j : break
                #if find one char is different, break
                if s[j]!=strs[i][j]: break
                #else, length of same chars plus 1
                temp+=1
            #renew the length
            count = temp
            
        if count<0:return ""
        else: return s[0:count+1]
                
                
