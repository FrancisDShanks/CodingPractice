# straight foward solution
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym1 = ['M','D','C','L','X','V','I']
        sym2=["CM","CD","XC","XL","IX","IV"]
        rad1=[1000,500,100,50,10,5,1]
        rad2=[900,400,90,40,9,4]
        index = len(s) - 1
        index1 = 6
        index2 = 5
        res = 0
        while index>=0:
            if index1>=0:
                while s[index]==sym1[index1] and index>=0:
                    index -= 1
                    res += rad1[index1]
            if index2>=0:
                while s[index-1:index+1] == sym2[index2] and index >= 0:
                    index -= 2
                    res += rad2[index2]
            index1 -= 1
            index2 -= 1
        return res


    
    
    
    
    
# faster algorithm
#如果不出现减的情况,整个roman串应该是从左到右变小的,所以如果当前字符比前一个字符小(或相等),那就加上这个字符代表的数
#如果是出现减的情况,比如IV,那么当前字符就比前一个字符大,前一个字符多加了一次,所以加上(-2*pre+cur)
# 对于IV,就是先多加了一个1再加(-2+5)
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000,
             'D':500,
             'C':100,
             'L':50,
             'X':10,
             'V':5,
             'I':1
            }
        pre = 4000
        res = 0
        for letter in s:
            cur = d[letter]
            if cur <= pre:
                res += cur
                pre = cur
            else:
                res = res - 2*pre + cur
        return res
