/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> s;
        TreeNode *cur = root;
                
        while(!s.empty() or cur!=NULL){
            if (cur!=NULL){
                res.push_back(cur->val);
                s.push(cur);
                cur = cur->left;
            }
            else{
                cur = s.top();
                s.pop();
                cur = cur->right;
            }
        }
        return res;
    }
};




/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 #include <stack>
 
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> traversal;
        stack<TreeNode*> s;
        if(root!=NULL) s.push(root);
        
        while(!s.empty()){
            TreeNode *temp = s.top();
            s.pop();
            if(temp->right!=NULL) s.push(temp->right);
            if(temp->left!=NULL) s.push(temp->left);
            traversal.push_back(temp->val);
        }
        return traversal;
    }
};
