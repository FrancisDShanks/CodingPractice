#Working on Link Code
#Author:Francis Du
#Date:  02/16/2016
#Problem: Search a 2D Matrix
#Errors I made:
#               1.the last row need to be handled carefully, which I haven't.
#Things needs to be noticed:
#               The two binary searches have different condition
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False
        
        n = len(matrix)-1
        m = len(matrix[0])-1
        start = 0
        end = n
        
        while start+1 < end:
            if target<matrix[start][0] :
                return False
            if target>matrix[end][0]:
                start = end
                break
            if target == matrix[start][0] or target == matrix[end][0]:
                return True
            mid = (start + end) / 2
            if target < matrix[mid][0]:
                end = mid
            else:
                start = mid
                
        row  = start
        start = 0
        end = m
        while start <= end:
            if target == matrix[row][start] or target == matrix[row][end]:
                return True
            if target<matrix[row][start] or target>matrix[row][end]:
                return False

            mid = (start + end) / 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                end  = mid-1
            else:
                start = mid+1
        
        return False
