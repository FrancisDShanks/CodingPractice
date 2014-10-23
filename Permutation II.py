# -*- coding: utf-8 -*-
'''
Created on Oct 23, 2014

@author: Xufan Du
@email: tctcdtc@gmail.com

'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num)==0: return []
        num.sort()
        visited = [0 for i in range(0,len(num))]
        Solution.res = []
        self.DFS(num,0,[],visited)
        return Solution.res
        
    def DFS(self,num,level,cur,visited):
        if level == len(num):
            Solution.res.append(cur)
            return
        for i in range(0,len(num)):
            if visited[i]==0:
                if i>0 and num[i]==num[i-1] and visited[i-1]==0:
                    continue
                visited[i]=1
                self.DFS(num,level+1,cur+[num[i]],visited)
                visited[i]=0
