# solution - 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
        
# solution - 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        if x < 0:
            return False
        dup = x
        new_x = 0
        while dup > 0:
            new_x = new_x*10 + dup % 10
            dup = dup // 10
            
        if new_x != x:
            return False
        return True
   
   
# solution - 3 (fail)
# failed on case : 10000021
# in this solution, case 10000021 will treat 000002 as 2 and return True
# maybe we can add a mark to 000002
class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        if x < 0:
            return False
        while x > 9:
            right = x % 10
            x = x // 10
            tmp = 10 ** int(math.log10(x))
            left = x // tmp
            x = x - left * tmp
            if right != left:
                return False
        return True
            
            
