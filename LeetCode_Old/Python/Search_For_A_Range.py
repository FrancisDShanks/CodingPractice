class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self.binarySearchmostleft(A,target),self.binarySearchmostright(A,target)]
        
    def binarySearchmostleft(self,li,tar):
        if len(li)==0: return None
        if len(li)==1: 
            if tar==li[0]:
                return 0
            else:
                return -1
        right = len(li)-1
        left = 0
        while(left<=right):
            mid = (left+right)/2
            if li[mid]==tar:
                if  mid>left and li[mid-1]==tar:
                    right=mid-1
                    continue
                else:
                    return mid
            elif li[mid]<tar:
                left=mid+1
            else:
                right=mid-1
        return -1
    
    def binarySearchmostright(self,li,tar):
        if len(li)==0: return None
        if len(li)==1: 
            if tar==li[0]:
                return 0
            else:
                return -1
        right = len(li)-1
        left = 0
        while(left<=right):
            mid = (left+right)/2
            if li[mid]==tar:
                if mid<right and li[mid+1]==tar:
                    left=mid+1
                    continue
                else:
                    return mid
            elif li[mid]<tar:
                left=mid+1
            else:
                right=mid-1
        return -1   
