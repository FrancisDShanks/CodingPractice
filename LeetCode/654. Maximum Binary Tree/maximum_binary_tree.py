# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        m = nums.index(max(nums))
        node = TreeNode(nums[m])
        node.left = self.constructMaximumBinaryTree(nums[:m])
        node.right = self.constructMaximumBinaryTree(nums[m+1:])
        return node
