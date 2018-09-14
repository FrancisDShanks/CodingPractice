# using the idea of Backtracking
# see helper function
class Solution:
    def helper(self,start,n,k,tmp):
        if len(tmp) == k:
            self.res.append([i for i in tmp])
            return
        for i in range(start,n+1):
            tmp.append(i)
            self.helper(i+1,n,k,tmp)
            tmp.pop()
        return
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        tmp = []
        if k>n or n<1 or k<1:return self.res
        self.helper(1,n,k,tmp)
        return self.res
        
        
# or use python library
class Solution:        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools
        nums = [i for i in range(1,n+1)]
        return [i for i in itertools.combinations(nums,k)]
