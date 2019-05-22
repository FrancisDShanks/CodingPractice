class Solution(object):
    # 如果数据量大的话,拆分成负数和非负数两个数组,平方之后在merge.应该比排序好,毕竟排序是nlogn的.做题就将就了
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x*x for x in A])
        
