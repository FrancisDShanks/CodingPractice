class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int c0 = cost[0];
        int c1 = cost[1];
        int tmp = 0;
        for(int i=2;i<cost.size();i++){
            tmp = c1;
            c1 = min(c0,c1)+cost[i];
            c0 = tmp;
        }
        return min(c0,c1);
    }
};
