# 考察细节的题目,各种边界条件
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            i = 0
            j = 0
            flag = True
            while i < len(S) and j < len(word):
                if S[i] != word[j]:
                    flag = False
                    break
                tmp = S[i]
                cnti = 1
                cntj = 1
                while i + 1 < len(S) and S[i + 1] == tmp:
                    i += 1
                    cnti += 1
                while j + 1 < len(word) and word[j + 1] == tmp:
                    j += 1
                    cntj += 1
                    
                # if cnti=cntj ok
                # if cnti<cntj not ok
                # if cnti>=cntj>=3 ok                
                # if cntj=1,cnti=2 not ok
                # if (cntj=1 or cntj=2), cnti>=3 ok
                if cnti < cntj or (cntj == 1 and cnti == 2):
                    flag = False
                    break
                i += 1
                j += 1
            # remember to check if there are remainings
            if flag and i == len(S) and j == len(word):
                cnt += 1
        return cnt
                

                
