#solution - 1 原始的分支判断 Runtime: 36 ms
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q','w','e','r','t','y','u','i','o','p'}
        row2 = {'a','s','d','f','g','h','j','k','l'}
        row3 = {'z','x','c','v','b','n','m'}
        res = []
        for word in words:
            if word:
                w = word.lower()
                flag = True
                if w[0] in row1:
                    for letter in w:
                        if letter not in row1:
                            flag = False
                            break
                elif w[0] in row2:
                    for letter in w:
                        if letter not in row2:
                            flag = False
                            break
                else:
                    for letter in w:
                        if letter not in row3:
                            flag = False
                            break
                if flag:
                    res.append(word)
        return res
                    
               
#solution - 2, 运用集合 Runtime: 36 ms
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {'q','w','e','r','t','y','u','i','o','p'}
        row2 = {'a','s','d','f','g','h','j','k','l'}
        row3 = {'z','x','c','v','b','n','m'}
        res = []
        for word in words:
            w = set(word.lower())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                res.append(word)
        return res
        
#solution - 3
# 语法糖
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('zxcvbnm'),set('asdfghjkl'),set('qwertyuiop')]
        return [word for word in words if list(filter(lambda x:set(word.lower()).issubset(x),rows))]
        
                    
                
