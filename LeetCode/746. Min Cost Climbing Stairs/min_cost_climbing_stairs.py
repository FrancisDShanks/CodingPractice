# a simple dynamic programming problem
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = [0 for _ in range(0,len(cost)+1)]
        for i in range(2,len(cost)+1):
            res[i] = min(res[i-2]+cost[i-2],res[i-1]+cost[i-1])
        return res[-1]
        

# after some optimization
# no need to build an array to store all the sum history
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        tmp1,tmp2 = cost[0],cost[1]
        for i in cost[2:]:
            tmp1,tmp2 = tmp2, min(tmp1,tmp2)+i
        return min(tmp1,tmp2)
        
