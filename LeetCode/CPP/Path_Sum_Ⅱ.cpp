/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    vector<vector<int>> m;    
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        m.clear();
        if(!root) return m;
        
        vector<int> v;

        find(root,sum,v);
        return m;
    }
    
    void find(TreeNode *root,int sum,vector<int> v){
        if(!root) return;
        v.push_back(root->val);
        if(root->left==NULL && root->right==NULL && sum==root->val){
            m.push_back(v);
            return;
        }
        
        find(root->left,sum-root->val,v);
        find(root->right,sum-root->val,v);
        return;
    }
};
