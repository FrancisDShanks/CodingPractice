#二分搜索法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        lo = 0
        hi = num
        while lo < hi:
            mid = lo + (hi - lo) // 2 
            if mid * mid == num:
                return True
            elif mid * mid > num:
                hi = mid
            else:
                lo = mid + 1
        return False
        
        
        
        
        
# 其他方法:
#   牛顿法
#   Math Trick for Square number is 1+3+5+ ... +(2n-1)
#   位运算
