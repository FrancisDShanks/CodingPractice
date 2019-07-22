# classic problem : find the k-th number in two sorted arrays
# for this problem, k = (len(array1) + len(array2)) / 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2)) // 2 
        def findkth(n1, n2, k):
            if not n1:
                return n2[k - 1]
            if not n2:
                return n1[k - 1]
            if k == 1:
                return min(n1[0], n2[0])            
            k1 = k // 2
            #print(k1, k)
            if len(n1) <= k1:               
                k1 = len(n1)
                k2 = k - k1
            if len(n2) <= k1:              
                k2 = len(n2)
                k1 = k - k2
            else:              
                k2 = k - k1
            # print(n1, n2, 'k=',k, 'k1=',k1, 'k2=',k2)
            if n1[k1 - 1] == n2[k2 - 1]:
                return n1[k1 - 1]
            elif n1[k1 - 1] < n2[k2 - 1]:
                return findkth(n1[k1:], n2, k - k1)
            else:
                return findkth(n1, n2[k2:], k - k2)            
        if (len(nums1) + len(nums2)) % 2 == 1:
            return findkth(nums1, nums2, k + 1)
        else:
            return (findkth(nums1, nums2, k) + findkth(nums1, nums2, k + 1)) / 2
