# problem about backtraking

# solution 1 - 172ms in leetcode
class Solution:
    def helper(self,candidates,target,tmp,i):
        if target == 0:
            self.res.append([t for t in tmp])
            return
        if target < 0 or i>=len(candidates): return

        for j in range(0,target//candidates[i]+1):
            self.helper(candidates,target-(candidates[i]*j),tmp+[candidates[i]]*j,i+1)
        return
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        tmp = []
        self.helper(candidates,target,tmp,0)
        return self.res
        
# solution 2 - 76ms in leetcode
class Solution:
    def helper(self,candidates,target,tmp,i):
        if target < 0: 
            return
        elif target == 0:
            self.res.append([t for t in tmp])
            return
        else:
            while (i<len(candidates)) and (target-candidates[i]>=0):
                tmp.append(candidates[i])
                self.helper(candidates,target-candidates[i],tmp,i)
                i+=1
                tmp.pop()
        return
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        tmp = []
        self.helper(sorted(candidates),target,tmp,0)
        return self.res
      
# solution 3 - 64ms in leetcode
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(remain, stack):
            if not remain:
                res.append(stack)
                return 
            for item in candidates:
                if item > remain:
                    break
                elif not stack or item >= stack[-1]:
                    dfs(remain - item, stack + [item])
        dfs(target, [])
        return res
