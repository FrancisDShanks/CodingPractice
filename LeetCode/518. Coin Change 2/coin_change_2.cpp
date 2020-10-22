//完全背包问题
//变化是正好要求背包装满（正好凑齐amount）并计算方案总数

class Solution {
public:
    int change(int amount, vector<int>& coins) {

        int n = coins.size();
        int dp[amount+1];
        
        //初始化dp数组
        //如果amount=0的情况,那就只有1种取法:一个都不取,所以dp[0]=1
        //其他的位置表示amount=1,2...,n,而没有硬币,怎么都凑不成,所以其他位置都初始化为0
        memset(dp,0,sizeof(dp));
        dp[0] = 1;
        
        for(int i=0;i<n;++i){
            for(int j=coins[i];j<=amount;++j){
                dp[j] += dp[j-coins[i]];
            }
        }
        
        return dp[amount];
    }
};






        
