# dynamical programming problem
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        res[0][0] = 1
        
        mark = 1
        for i in range(n):
            if mark and obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                res[i][0] = 0
                mark = 0
                
        mark = 1
        for i in range(m):
            if mark and obstacleGrid[0][i] == 0:
                res[0][i] = 1
            else:
                res[0][i] = 0
                mark = 0
                
        
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[n-1][m-1]


# similiar solution
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        res = [[0 for _ in range(m)] for _ in range(n)]
        res[0][0] = 1
        for i in range(n):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                for j in range(i,n):
                    res[j][0] = 0
                break
        for i in range(m):
            if obstacleGrid[0][i] == 0:
                res[0][i] = 1
            else:
                for j in range(i,m):
                    res[0][j] = 0
                break
        
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[n-1][m-1]
