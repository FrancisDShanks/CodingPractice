# 可以用DFS或者BFS, 也可以用并查集做
# recursive 
class Solution:
    def dfs(self, grid, i, j):
        if i == -1 or j == -1 or i == len(grid) or j == len(grid[0]) or self.visit[i][j]:
            return
        if grid[i][j] == '0':
            self.visit[i][j] = True
            return
        self.visit[i][j] = True
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        return
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ret = 0
        self.visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    self.visit[i][j] = True
                elif not self.visit[i][j]:
                    self.dfs(grid, i ,j)
                    ret += 1
        return ret
                

# iterative
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ret = 0
        r = len(grid)
        c = len(grid[0])
        stack = []
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    continue
                stack.append((i, j))
                
                while stack:
                    a, b = stack.pop()
                    grid[a][b] = '0' # 这里访问过的设为'0'就可以防止重复访问
                    if a - 1 > -1 and grid[a - 1][b] == '1':
                        stack.append((a-1, b))
                    if a + 1 < r and grid[a + 1][b] == '1':
                        stack.append((a+1, b))
                    if b - 1 > -1 and grid[a][b - 1] == '1':
                        stack.append((a, b-1))
                    if b + 1 < c and grid[a][b + 1] == '1':
                        stack.append((a, b+1))
                ret += 1
        return ret
