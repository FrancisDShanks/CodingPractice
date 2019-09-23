# 这个题是个回退的思想，或者说像题目标注的类型是stack的思想
# 思想是：
#   1. 先找到K这个index在最后解码的串中的位置，只需要找到位置而不需要真正的解码这个串（会超时/内存不够），看题目给的'a'那个样例也知道不能真正解码构建结果
#   2. 然后根据找到的位置,反过来倒推(stack思想,回退思想). 整个过程和1是逆向的
#        1)如果当前字符是数字,那么前面size*m,这里就/m,逆向。 同时K=K%size，因为吗m*size缩小到size，而缩小前的m*size其中第K个和第K%size个是一样的，因为本来就是重复得来的
#        2)如果当前字符是字母,如果K=0或者K=size就说明正好找到.不然size=size-1,逆向.
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # find where K is
        size = 0
        cnt = -1
        for s in S:
            if size >= K:
                break
            
            size = size + 1 if not s.isdigit() else size * int(s)
            cnt += 1
            
            
                
                
        # track back
        for j in range(cnt, -1, -1):
            if S[j].isdigit():
                size /= int(S[j])
                K %= size
            else:
                if K == 0 or size == K:
                    return S[j]
                size -= 1
        
