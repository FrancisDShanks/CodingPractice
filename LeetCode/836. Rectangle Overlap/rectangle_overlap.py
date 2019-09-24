# 很简单的题目,只要想对了解法..
# 先看1D的情况,两个线段x1x2和y1y2
# 要x1x2与y1y2相交,必须有x1<y2 and y1<x2
# 包含了所有情况
# 推广到2D,就是两个维度都满足上面的情况,就可以判断了

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0]<rec2[2] and rec2[0]<rec1[2] and rec1[1]<rec2[3] and rec2[1]<rec1[3]


# 最开始的提交,想多了..
class Solution(object):
    def point_in_rec(self, x, y, rec):
        return rec[0] < x and x < rec[2] and rec[1] < y and y < rec[3]
        
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """


        if (rec2[0] > rec1[2]) or (rec2[2] < rec1[0]):
            return False
        if (rec2[1] > rec1[3]) or (rec2[3] < rec1[1]):
            return False
        
        # centre
        if self.point_in_rec((rec1[0]+rec1[2])/2, (rec1[1]+rec1[3])/2, rec2):
            return True
        if self.point_in_rec((rec2[0]+rec2[2])/2, (rec2[1]+rec2[3])/2, rec1):
            return True

        # for corner
        if self.point_in_rec(rec1[0], rec1[1], rec2) or self.point_in_rec(rec1[0], rec1[3], rec2) or \
            self.point_in_rec(rec1[2], rec1[1], rec2) or self.point_in_rec(rec1[2], rec1[3], rec2):
            return True
        
        # four edge
        for y in range(rec1[1], rec1[3] + 1):
            if self.point_in_rec(rec1[0], y, rec2) or self.point_in_rec(rec1[2], y, rec2):
                return True
            
        for x in range(rec1[0], rec1[2] + 1):
            if self.point_in_rec(x, rec1[1], rec2) or self.point_in_rec(x, rec1[3], rec2):  
                return True
        return False
