        
# using a stack
# O(n) time, extra O(n) space
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def remove_backspace(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        
        return remove_backspace(S) == remove_backspace(T)
        
        
# using a helper function
# O(n) time and O(1) space
# 45.80% runtime
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(A, n):
            cnt = 0
            while n >= 0 and (A[n] == '#' or cnt):
                    while n >= 0 and A[n] == '#':
                        cnt += 1
                        n -= 1
                    while n >= 0 and A[n] != '#' and cnt > 0:
                        cnt -= 1
                        n -= 1
            return n
            
        i, j = len(S) - 1, len(T) - 1
        while i >= 0 and j >= 0:
            if S[i] != '#' and T[j] != '#':
                if S[i] != T[j]:
                    return False
                i -= 1
                j -= 1
            else:
                i = helper(S, i)
                j = helper(T, j) 
        
        i = helper(S, i)
        j = helper(T, j)
        if i >= 0 or j >= 0:
            return False
        return True
        
        
        
# 95.10% runtime
# don't use the helper
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        while i >= 0 and j >= 0:
            if S[i] != '#' and T[j] != '#':
                if S[i] != T[j]:
                    return False
                i -= 1
                j -= 1
            else:
                cnt = 0
                while i >= 0 and (S[i] == '#' or cnt):
                    while i >= 0 and S[i] == '#':
                        cnt += 1
                        i -= 1
                    while i >= 0 and S[i] != '#' and cnt > 0:
                        cnt -= 1
                        i -= 1
                
                cnt = 0
                while j >= 0 and (T[j] == '#' or cnt):
                    while j >= 0 and T[j] == '#':
                        cnt += 1
                        j -= 1
                    while j >= 0 and T[j] != '#' and cnt > 0:
                        cnt -= 1
                        j -= 1                
        
        cnt = 0
        while i >= 0 and (S[i] == '#' or cnt):
            while i >= 0 and S[i] == '#':
                cnt += 1
                i -= 1
            while i >= 0 and S[i] != '#' and cnt > 0:
                cnt -= 1
                i -= 1
                
        cnt = 0
        while j >= 0 and (T[j] == '#' or cnt):
            while j >= 0 and T[j] == '#':
                cnt += 1
                j -= 1
            while j >= 0 and T[j] != '#' and cnt > 0:
                cnt -= 1
                j -= 1 
        if i >= 0 or j >= 0:
            return False
        return True
        
        
        
        

        
