# solution - 1
# simulate the inserting process
# fast and less memory space cost, but coding takes more time, lol
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        for q in queries:
            i = 0
            j = 0
            tmp = True
            while i < len(q) and j < len(pattern):
                if q[i] == pattern[j]:
                    j += 1
                    i += 1
                elif 97 <= ord(q[i]) <= 122: 
                    i += 1
                else:
                    # if there is more Upper letter than pattern, return false
                    tmp = False
                    break
            # if the word is ending but there exist letter in pattern not been matched, return false
            if i == len(q) and j < len(pattern):
                tmp = False
            # else, the pattern is used up, make sure the letters left in word are all lower case letters
            elif j == len(pattern):
                while i < len(q):
                    if not (97 <= ord(q[i]) <= 122):
                        tmp = False
                        break
                    i += 1
            ret.append(tmp)
        return ret
                    
                    
                    
# solution - 2
# using re module to do regex matching
# slow than solution 1, but easy coding
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        insert_low = '[a-z]*'
        new_pattern = insert_low
        for p in pattern:
            new_pattern = new_pattern + p + insert_low
        new_pattern = '^' + new_pattern + '$'
        return [True if re.match(new_pattern, q) else False for q in queries ]
                    
