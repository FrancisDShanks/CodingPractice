# recursion solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(node1,node2):
            if not node1 and not node2:return True
            if node1 and not node2 or not node1 and node2: return False
            if node1.val != node2.val: return False
            return isSym(node1.left,node2.right) and isSym(node1.right,node2.left)
        
        if not root: return True
        return isSym(root.left,root.right)
        
      
      
 # iteration solution - beat 99.82% leetcode
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        if not root: return True
        s = [root.left,root.right]
        while s:
            node1 = s.pop()
            node2 = s.pop()
            if node1 is None and node2 is None: 
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            # I choose dont't use s+=[]
            # when I code this problem, I wondered should I choose s+=[] or s.append(). so I did a simple test
            # the result is that: s.append() is about 80 times faster than s+=[], (running 1000 times)
            s.append(node1.left)
            s.append(node2.right)
            s.append(node1.right)
            s.append(node2.left)
        return True
                
