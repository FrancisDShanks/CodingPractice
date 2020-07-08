//最优解法应该是两次翻转发
// [1,2,3,4,5,6,7], k=3
// 第一次以k为界翻转左右两部分 -> [4,3,2,1,7,6,5]
// 第二次翻转整个数组 -> [5,6,7,1,2,3,4]
//空间复杂度O(1),时间复杂度O(n)

class Solution {
public:
    void reverse(vector<int>& nums, int start, int end){
        int tmp = 0;
        while (start<end){
            tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;            
        }
        return;
    }
    
    void rotate(vector<int>& nums, int k) {
        if(k<1 or nums.size()==0) return;
        k = k % nums.size(); //注意先处理k值
        reverse(nums, 0, nums.size() - k - 1);
        reverse(nums, nums.size() - k, nums.size() - 1);
        reverse(nums, 0, nums.size() - 1);
        
    }
};
