# solution using string as key
# this soslution can work in more generic situations
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        res = 0
        for dominoe in dominoes:
            s = ' '.join([str(i) for i in sorted(dominoe)])
            if s in d:
                res += d[s]
                d[s] += 1
            else:
                d[s] = 1
        return res




# since all dominoes[i][j] is in range 1 ~ 9
# so this solution use min(dominoe) * 10 + max(dominoe) as key
# if dominoes[i][j] can be larger than 10 and can be 0, this solution is wrong
# because [1,10] and [0,20] will be the same
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        res = 0
        for dominoe in dominoes:
            s = min(dominoe) * 10 + max(dominoe)
            res += d[s] if s in d else 0
            d[s] = d[s] + 1 if s in d else 1
        return res
