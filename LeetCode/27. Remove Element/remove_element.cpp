class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l = nums.size();
        int res = 0;
        for(int i=0;i<l;i++){
            if(nums[i] != val){
                nums[res] = nums[i];
                res++;
            }
        }
        return res;
        
    }
};