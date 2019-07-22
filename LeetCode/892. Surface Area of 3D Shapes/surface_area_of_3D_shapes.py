class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # bottom and top
                if grid[i][j] > 0:
                    res += 2
                # left
                # if not the first column, only count right to avoid duplicate calculation
                if i == 0:
                    res += grid[i][j]
                # right
                if i == len(grid) - 1:
                    res += grid[i][j]
                else:
                    res += abs(grid[i][j] - grid[i + 1][j])
                # front
                if j == 0:
                    res += grid[i][j]
                # back
                if j == len(grid[0]) - 1:
                    res += grid[i][j]
                else:
                    res += abs(grid[i][j] - grid[i][j + 1])
                    
        return res
