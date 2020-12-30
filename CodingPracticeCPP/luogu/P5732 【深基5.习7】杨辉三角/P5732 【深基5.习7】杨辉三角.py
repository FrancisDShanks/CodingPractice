# Author: FrancisDShanks
# Email: tctcdtc@gmail.com

n = int(input())
a = [[0 for i in range(n+1)] for j in range(n+1)]
a[1][1] = 1
print("1")
for i in range(2,n+1):
    for j in range(1,i+1):
        a[i][j] = a[i-1][j-1] + a[i-1][j]
        print(a[i][j],end=' ')
    print('')