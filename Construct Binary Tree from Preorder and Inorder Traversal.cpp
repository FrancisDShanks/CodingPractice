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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        if(preorder.empty() || inorder.empty()) return NULL;
        return b(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
    }
    
    TreeNode *b(vector<int> &preorder, int sp,int ep, vector<int> &inorder, int si,int ei){
        if(sp>ep || si>ei) return NULL;
        TreeNode *root = new TreeNode(preorder[sp]);
        if(sp==ep) return root;
        int in=0;
        for(int i=si;i<=ei;i++){
            if(inorder[i]==preorder[sp]){
                in=i;
                break;
            }
        }
        
        root->left = b(preorder,sp+1,sp+in-si,inorder,si,in-1);
        root->right = b(preorder,sp+in-si+1,ep,inorder,in+1,ei);
        return root;
    }
};
