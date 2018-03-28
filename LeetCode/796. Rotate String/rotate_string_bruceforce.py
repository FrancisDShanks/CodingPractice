# bruce force, slow solution
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:
            return True
        cnt = len(A)
        while cnt > 0:
            if A == B:
                return True
            A = A[1:] + A[0]
            cnt -= 1