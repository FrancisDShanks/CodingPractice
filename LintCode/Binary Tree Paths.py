"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if root==None:
            return []
        return self.DFS(root)
            
    def DFS(self,node):
        if node.left == None and node.right == None:
            return [str(node.val)]
        res = []
        
        if node.left!=None:
            tmp = self.DFS(node.left)
            for i in range(0,len(tmp)):
                res.append(str(node.val)+"->"+tmp[i])
        
        if node.right!=None:
            tmp = self.DFS(node.right)
            for i in range(0,len(tmp)):
                res.append(str(node.val)+"->"+tmp[i])
        return res
        
            
