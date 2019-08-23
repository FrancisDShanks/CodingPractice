class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        o = 1
        e = 0
        while o < len(A) and e < len(A):
            if A[e] % 2 == 1:
                while A[o] % 2 == 1:
                    o += 2
                A[o], A[e] = A[e], A[o]
            e += 2
        return A


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        e = []
        o = []
        for i, a in enumerate(A):
            if i % 2 == 0 and a % 2 == 0:
                continue
            elif i % 2 == 1 and a % 2 == 1:
                continue
            elif i % 2 == 0:
                o.append(i)
            else:
                e.append(i)
        for i in range(len(o)):
            A[o[i]], A[e[i]] = A[e[i]], A[o[i]]
        return A
            
            
