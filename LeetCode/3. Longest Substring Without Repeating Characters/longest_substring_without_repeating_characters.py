# solution - 1
# using a slicing window to simulate the substring with no duplicate
# the window is s[slow] ~ s[fast], the length is fast - slow + 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        slow = 0
        fast = 0
        window = set()
        while fast < len(s):
            if s[fast] not in window:
                window.add(s[fast])
                fast += 1
            else:
                ret = max(ret, fast - slow) # length is actually (fast - slow + 1) but the fast is already plused one 
                window.remove(s[slow])
                slow += 1
        return max(ret, fast - slow)
                
                
# solution - 2            
# a modified version (faster)
# move the slicing window directly to location after the duplicate char's last appearence
# instead of move the window step by step
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        slow = 0
        fast = 0
        window = dict()
        cnt = 0
        while fast < len(s):
            if s[fast] not in window:
                window[s[fast]] = fast
                fast += 1
                cnt += 1
            else:
                ret = max(ret, cnt) 
                loc = window[s[fast]]
                while slow <= loc:
                    window.pop(s[slow])
                    slow += 1
                window[s[fast]] = fast
                
                cnt = fast - loc
                fast += 1
        return max(ret, cnt)
        
# solution -3
# a modified version, faster than solution - 2
# the slicing window is s[start + 1] ~ s[i], length is i - (start + 1) + 1 = i - start
# if the last appearence of a char is smaller than start, then ignore it as it is out of the slicing window.
# save time to delete element in the dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = -1
        d = {}
        ret = 0 
        for i in range(len(s)):
            
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i                
                
            else:
                d[s[i]] = i
                if i - start > ret:
                    ret = i - start
        return ret
