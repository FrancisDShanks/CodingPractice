//
//Created on April 21, 2014
//
//@author: Xufan Du
//

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
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        if(postorder.empty() || inorder.empty()) return NULL;
        return b(inorder,0,inorder.size()-1,postorder,0,postorder.size()-1);
    }
    
    TreeNode *b(vector<int> &inorder, int si,int ei, vector<int> &postorder, int sp,int ep){
        if(sp>ep || si>ei) return NULL;
        TreeNode *root = new TreeNode(postorder[ep]);
        if(sp==ep) return root;
        int in=0;
        for(int i=si;i<=ei;i++){
            if(inorder[i]==postorder[ep]){
                in=i;
                break;
            }
        }
        
        root->left = b(inorder,si,in-1,postorder,sp,sp+in-1-si);
        root->right = b(inorder,in+1,ei,postorder,sp+in-si,ep-1);
        return root;
    }
};
