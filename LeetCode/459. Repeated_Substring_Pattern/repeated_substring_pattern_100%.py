# a 100% solution found in leetcode discussion
# 对这个算法大概的理解如下,但是我一直没能理清如何证明这个算法:
# 因为根据提交情况可以知道,s本身不能作为自己的substring
# 所以符合pattern的s至少由2个或以上sub重复来构成
# 以s由2个sub构成为例:
# ss = s[1:]+s[:-1], ss由2个s组成,也就是由4个sub组成
# 去掉头尾的字符,破坏第一个sub和最后一个sub,中间应该2个sub,恰好构成s
# 所以如果s in ss就返回True
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = s[1:]+s[:-1]
        return s in ss
                
        
