# this question is a DP question
# variable cnt record the amount of dresses "pass through" the machine
# (dress - aver) represent this machine need how many dresses to hold the aver number of dresses
# so the result should be the max of abs(cnt) and (dress -aver)


class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = 0
        for dress in machines:
            total += dress
        if total%len(machines):
            return -1
        else:
            aver = total//len(machines)
        
        cnt = 0
        res = 0
        for dress in machines:
            cnt += (dress - aver)
            res = max(res,dress-aver,abs(cnt))
            
        return res
