# because comparing letters in ordering many times, and access list waste time
# so using a dict to store the order
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d_order = {value:index for index,value in enumerate(order)}
        
        for i in range(1,len(words)):
            first = words[i - 1]
            second = words[i]
            j = 0
            while j < len(first) and j < len(second):
                if d_order[first[j]] < d_order[second[j]]:
                    break
                if d_order[first[j]] > d_order[second[j]]:
                    return False
                j += 1
            if j == len(second) and j < len(first):
                return False
        
        return True
                
            
