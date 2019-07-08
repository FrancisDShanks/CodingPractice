# slicing window of siez 3
# or can use a sign of 1 and -1, because a < b > c then next is b > c < d which equals too -b < -c > -d
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A: return 0
        if len(A) == 1 or (len(A) == 2 and A[0] == A[1]) or len(set(A)) == 1: return 1
        if len(A) == 2: return 2
        
        ret = 2
        tmp = 2
        for i in range(2, len(A)):
            if (A[i-2] < A[i-1] and A[i-1] > A[i]) or (A[i-2] > A[i-1] and A[i-1] < A[i]):
                tmp += 1
                if tmp > ret:
                    ret = tmp
            else:
                tmp = 2
        return ret
                
