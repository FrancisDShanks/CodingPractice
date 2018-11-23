# solution 1 dynamical programming 
# solution 2 optimalized DFS with cache - recursion
# solution 3 optimalized DFS with cache - iteration
# checking https://www.cnblogs.com/grandyang/p/4298664.html  参考了大神的结题报告,各种解法

# solution 1
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        c = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        
        # 0 in the solution means 'empty'
        # c[1][3] means using first 1 chars in s1 and first 3 chars in s2
        c[0][0] = True
        
        for i in range(1,l1 + 1):
            if s1[i-1] == s3[i-1]:c[i][0] = True
            else:break
                
        for j in range(1,l2 + 1):
            if s2[j-1] == s3[j-1]:c[0][j] = True
            else:break
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s1[i-1] == s3[i+j-1] and c[i-1][j]:
                    c[i][j] = True
                if s2[j-1] == s3[i+j-1] and c[i][j-1]:
                    c[i][j] = True
        return c[l1][l2]
            

# solution 2 
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        
        def dfs(index1,index2,visited):
            if index1 == l1 and index2 == l2:
                return True
            if (index1,index2) in visited:
                return False
            if index1 < l1 and s1[index1] == s3[index1+index2] and dfs(index1+1,index2,visited):
                return True
            if index2 < l2 and s2[index2] == s3[index1+index2] and dfs(index1,index2+1,visited):
                return True
            visited.add((index1,index2))
            return False
            
            
        visited = set()
        return dfs(0,0,visited)
            
        
        
# solution 3
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        
        stack = [(0,0)]
        visited = set()
        while stack:
            i, j = stack.pop()           
        
            if i == l1 and j == l2:
                return True

            if i < l1 and s1[i] == s3[i+j] and (i+1,j) not in visited:
                stack.append((i+1,j))
                visited.add((i+1,j))
                                
            if j < l2 and s2[j] == s3[i+j] and (i,j+1) not in visited:
                stack.append((i,j+1))
                visited.add((i,j+1))
                
        return False     
            
            

            
