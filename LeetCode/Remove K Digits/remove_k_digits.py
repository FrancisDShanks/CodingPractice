class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # add a dummy '0' at the tail to avoid out of index
        num = num + '0'
        i = 0
        while i < len(num) - 1 and k > 0:
            # for case that the first char is removed then i = -1 after i -= 1
            if i < 0: i = 0
            if len(num) <= k:
                return '0'
            # if a char is larger than the next one, this one should be removed
            # then go back one step
            # if there are leading zeros now, it will be skipped(not removed and count k)
            if num[i] > num[i + 1]:
                num = num[:i] + num[i + 1:]
                k -= 1
                i -= 1
            else:
                i += 1
        # now all char is not larger than its next char
        # handle the remaining characters to be removed
        if k > 0 and len(num) <= k:
            return '0'
        elif k > 0:
            num = num[: -1 * k]
            
        # remove all leading zeros
        while num:
            if num[0] == '0':
                num = num[1:]
            else:
                break
        # return the result
        # if nothing left, return '0'
        # or cutting the dummy zero and return
        return num[:-1] if num else '0'
        
        
#  learned from other's submission, use stack to simulate the process
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        
        while k > 0:
            stack.pop()
            k -= 1
            
        return ''.join(stack).lstrip('0') or "0"
