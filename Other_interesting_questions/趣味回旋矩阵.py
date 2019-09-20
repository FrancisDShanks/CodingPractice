# 输入n，输出方阵，
# n=5时如下
# 0   0   0   0   5   
# 0   0   0   6   4   
# 0   0   7   14  3
# 0   8   15  13  2
# 9   10  11  12  1

# n=3时如下
# 0   0   3
# 0   4   2
# 5   6   1


# using numpy because the output of numpy is good looking, lol..
import numpy as np
def build(n):
    a = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    for i in range(n // 2):
        j = i
        while j < n - i * 2:
            a[i][j] = cnt
            cnt += 1
            j += 1
        ii = i
        j -= 1
        while ii < n - i and j > i:
            ii += 1
            j -= 1
            a[ii][j] = cnt
            cnt += 1
            
        while ii > i + 1:
            ii -= 1
            a[ii][j] = cnt
            cnt += 1        
    return a

def trans(a, size):
    for i in range(size):
        for j in range(size-i):
            a[i][j], a[size-1-j][size-1-i] = a[size-1-j][size-1-i], a[i][j]
    return a
    
def main():
  size = 13
  a = np.array(build(size))
  print(trans_two(a,size))
