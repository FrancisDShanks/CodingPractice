# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            self._binaryTreePaths(root, [])
        return self.result
        
    def _binaryTreePaths(self, node, path):
        if not node.left and not node.right:
            self.result.append('->'.join(path + [str(node.val)]))
            return
        # 这里要小心不要用append那会改变path内容, 用赋值是生成局部的path, 用来回溯
        path = path + [str(node.val)]
        if node.left:
            self._binaryTreePaths(node.left, path)
        if node.right:
            self._binaryTreePaths(node.right, path)
            

            
        
        
