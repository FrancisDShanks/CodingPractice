class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #simple dynamic programming
        #step[n] = step[n-1] + step[n-2]
        #step[0] = 0, step[1] = 1, step[2] = 2
        step = []
        step.append(0)
        step.append(1)
        step.append(2)
        for i in range(3, n + 1):
            step.append(step[i-1] + step[i-2])
        return step[n]
        
        
        
        
        
        
#if we want a faster solution:
#   there is no need to store the whole dp table for this question, just remember the previous one and the previous of the previous one
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        prepre = 1
        pre = 2
        for i in range(3, n + 1):
            tmp = pre + prepre
            prepre = pre
            pre = tmp
        return pre
