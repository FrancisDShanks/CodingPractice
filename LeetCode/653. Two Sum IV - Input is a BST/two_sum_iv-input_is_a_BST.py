# can use dict and tree traversal
# like dict + BFS or dict + DFS
# also can make use of BST, like the code below

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        l = self.inorder(root)
        left = 0
        right = len(l) - 1
        while left < right:
            if l[left] + l[right] == k:
                return True
            elif l[left] + l[right] < k:
                left += 1
            else:
                right -= 1
        return False

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

