class Solution:
    def fib(self, N: int) -> int:
        F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        return F[N]
        
        
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        i, a, b = 1, 0, 1
        while i < N:
            a, b = b, a + b
            i += 1
        return b
    
        
