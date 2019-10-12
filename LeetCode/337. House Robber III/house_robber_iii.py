# 可以用纵向的dp来理解
# dp[r]表示r结点及其所有子树的最优解

# 如果结点r访问,那么r.left和r.right都不能访问
# 如果不访问结点r,那么结果是dp[r.left]+dp[r.right]

# 所以dp公式为:
# dp[r] = max(dp[r.left]+dp[r.right],
#           dp[r.left.left]+dp[r.left.right]+dp[r.right.left]+dp[r.right.right]+r.val)
# 初始条件是r为叶子结点时 dp[r] = r.val

class Solution:
    def helper(self, node):
        if not node:
            return 0, 0, 0
        l,ll,lr = self.helper(node.left)
        r,rl,rr = self.helper(node.right)
        dp = max(l+r, ll+lr+rl+rr+node.val)
        return dp, l, r
    
    def rob(self, root: TreeNode) -> int:
        return self.helper(root)[0]
        
        
