/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isbt;
    int helper(TreeNode* node) {
        if (!isbt) return 0;
        if (!node) return 0;
        
        int rh = helper(node->right);
        int rl = helper(node->left);
        if (!isbt) return 0; //这里加一个判断从28ms 60%提升到16ms 90%
        
        
        int dif = abs(rh - rl);
        
        if (dif > 1){
            isbt = false;
            return 0;
        }
        return max(rh, rl) + 1;
            
    }
    
    bool isBalanced(TreeNode* root) {
        isbt = true;
        int height = helper(root);
        return isbt;   
        
    }
};
