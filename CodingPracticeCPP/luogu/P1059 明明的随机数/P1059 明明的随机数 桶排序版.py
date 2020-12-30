# Author: FrancisDShanks
# Email: tctcdtc@gmail.com

if __name__ == "__main__":
    n = int(input())
    a = [False] * 1001
    cnt = 0
    tmp = [int(i) for i in input().strip().split()]
    for i in range(len(tmp)):
        if not a[tmp[i]]:
            cnt += 1
        a[tmp[i]] = True
    print(cnt)
    for i in range(1,1001):
        if a[i]:
            print(i,end=' ')
        
