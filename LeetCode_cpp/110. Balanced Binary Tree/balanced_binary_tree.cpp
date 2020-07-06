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
    int helper(TreeNode* node, bool *isbt) {
        if (node->left == null and node->right == null){
            isbt = true;
            return 0;
        }
        
        bool isr = false;
        bool isl = false;
        int rh = helper(node->right, isr);
        int rl = helper(node->left, isl);
        
        if (isr == false or isl == false) return 0;
        int dif = rh - rl;
        if (dif < 0) dif = dif * (-1);
        if (dif == 0 or dif == 1){
            isbt = true;
            return dif;
        }
        else{
            return 0;
        }
            
    }
    
    bool isBalanced(TreeNode* root) {
        bool isbt = false;
        int height = helper(root, isbt);
        return isbt;   
        
    }
};
