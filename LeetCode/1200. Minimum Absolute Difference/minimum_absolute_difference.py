# beacause the goal is the minimal difference, so sort first
# than the minimal difference must be arr[i]-arr[i-1]
# than scan the list and renew the dif if new minial dif is found
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        a = sorted(arr)
        dif = a[1] - a[0]
        ret = [[a[0],a[1]]]
        for i in range(2, len(a)):
            d = a[i]-a[i-1]
            if d < dif:
                ret = [[a[i-1],a[i]]]
                dif = d
            elif d == dif:
                ret.append([a[i-1],a[i]])
        return ret
        
