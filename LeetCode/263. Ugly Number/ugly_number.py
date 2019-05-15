class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:  #made a mistake here, didn't consider num=0 case which will cause an infinite loop
            return False
        if num == 1:
            return True
        
        while num // 2 == num / 2:
            num = num // 2
            
        while num // 3 == num / 3:
            num = num // 3
        
        while num // 5 == num / 5:
            num = num // 5
        
        return num == 1 
