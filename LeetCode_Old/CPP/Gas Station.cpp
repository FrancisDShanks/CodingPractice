class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int sum=0;
        int total=0;
        int index=0;
        for(int i=0;i<gas.size();i++){
            total+=gas[i]-cost[i];
            if(sum<0) {sum=0;index=i;}
            sum+=gas[i]-cost[i];
            
        }
        return total>=0?index:-1;
    }
};
