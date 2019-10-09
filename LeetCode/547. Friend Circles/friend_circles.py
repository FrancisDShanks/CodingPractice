# 经典的并查集解法
# Union-Find 
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = [i for i in range(len(M))] # 用数组放并查集,初始全为根节点
        
        # 并
        def union(a, b):
            ap = find(a)
            bp = find(b)
            if ap == bp:
                return True
            uf[ap] = bp
            return True
            
        # 查
        def find(a):
            f = a
            while uf[f] != f:
                f = uf[f]
            return f
        
        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if not M[i][j]:
                    continue
                union(i, j)
        
        # 返回根节点的数量
        ret = 0
        for index, value in enumerate(uf):
            if value == index:
                ret += 1
        return ret
            
                
 # 带访问记录的DFS方法
 class Solution:
    def dfs(self, i, M):
        self.visit[i] = True
        for j in range(len(M)):
            if i != j and M[i][j] and not self.visit[j]:
                self.dfs(j, M)
                
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.visit = [False] * len(M)
        ret = 0
        for i in range(len(M)):
            if not self.visit[i]:
                self.dfs(i, M)
                ret += 1
        return ret
            
   
        
