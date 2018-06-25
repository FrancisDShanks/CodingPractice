class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # this is exactly a D-P problem
        A.sort()
        d = dict()
        l = len(A)

            
        for i in range(l):
            d[A[i]] = 1
            for j in range(i):
                if A[i]%A[j]==0 and A[i]//A[j] in d.keys():
                    d[A[i]] += d[A[j]] * d[A[i]//A[j]] 
                

        res = sum(d.values())
        return res%(10 ** 9 + 7)
