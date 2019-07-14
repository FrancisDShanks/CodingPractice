# keep the grid's all rows and all columns's max value unchanged
# and make all cells in the grid as large as possible

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0 
        row = [max(r) for r in grid]
        colum = [0] * len(grid[0])
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                colum[j] = max(colum[j], grid[i][j])
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt += (min(row[i], colum[j]) - grid[i][j])
        return cnt
                
