//完全背包问题
//变化是正好要求背包装满（正好凑齐amount）

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if(amount==0) return 0;
        int n = coins.size();
        int dp[amount+1];
        
        //初始化dp数组，因为要求最后要正好装满背包，求的又是最小问题(需要最少的硬币)
        //所以除了dp[0]其他都赋值为最大值
        //这里用amount+1就行了
        for(int j=1;j<=amount;j++){
            dp[j] = amount+1;
        }
        dp[0] = 0;
        
        for(int i=0;i<n;++i){
            for(int j=coins[i];j<=amount;++j){
                dp[j] = min(dp[j], dp[j-coins[i]]+1);
            }
        }
        
        if(dp[amount] > amount) return -1;
        else return dp[amount];
        
    }
};
