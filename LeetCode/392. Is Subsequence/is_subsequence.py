# solution - 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            index = t.find(c)
            if index == -1:
                return False
            t = t[index + 1:]
        return True
            

# solution - 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
        if i == len(s):
            return True
        return False


# solution for follow up question
# since there will be more than 1B s to compare with t
# different s are hard to be predicted, but t stays the same
# so we should memorize the features of t to save resource
# record all appearences of t and localtion of all the appearences
# use a dict of list or a list of list
# for example using dict of list here
# dict is to record all possible appearences of t
# each list record all location the appearence appears
# eg: t = 'amjnhanj'
# dict_t = { 'a':[0,5], 'm':[1], 'j':[2,7], 'n':[3,6] .....}
# the time complexity of the initialize dict_t take O(size(t)) time and O(size(t)) storage
# for a s
# search each char from s in dict_t
# eg: s='aj'
# for the first 'a', search it in dict_t['a'] which is [0,5]
# the search is a problem 'insert a number in a sorted list' which is a typical binary search problem
# it takes size(s) * O(log?) time
# details can be found in the following code

from collections import defaultdict
from bisect import bisect_left
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dt = defaultdict(list)
        for i, c in enumerate(t):
            dt[c].append(i)
        pre = 0
        for i, c in enumerate(s):
            loc = bisect_left(dt[c], pre)
            if loc == len(dt[c]):
                return False
            pre = dt[c][loc] + 1
            
        return True
