# the first solution is applying binary search two times, 
# first time is searching in first number of each row to find the correct row. 
# second time is searching in the row to try to find the number

# the second solution is applying binary search one times, treat the matrix as a long list

# solution 1
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        n = len(matrix)-1
        m = len(matrix[0])-1
        
        if target < matrix[0][0] or target > matrix[n][m]:
            return False
        
        findrow = n
        left = 0
        right = n
        
        while left<=right:
            mid = left + (right - left) // 2
            if target == matrix[mid][0] or target == matrix[mid][m]:
                return True
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target < matrix[mid][m]:
                findrow = mid
                break
            else:
                left = mid + 1
                
        left = 0
        right = m
        
        while left<right:
            mid = left + (right - left) // 2
            if target == matrix[findrow][mid]:
                return True
            elif target > matrix[findrow][mid]:
                left = mid + 1
            else:
                right = mid      
                
        return False
        
        
        
        
        
        
        
# solution 2 - a better solution
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        # notice here, n and m should be the length and width, not (length-1) and (width-1)
        n = len(matrix)
        m = len(matrix[0])         
        first = 0
        # notice the last should be n*m not n*m-1
        # the binary search algorithm I used is for boundary [first,last)
        # last should be (n*m-1)+1
        # where (n*m-1) is the index of the last number in matrix
        last = n * m 
        
        while first < last:
            
            mid = first + (last - first) // 2
            cur = matrix[mid//m][mid%m]
            if target == cur:
                return True
            elif cur < target:
                first = mid + 1
            else:
                last = mid
        return False
