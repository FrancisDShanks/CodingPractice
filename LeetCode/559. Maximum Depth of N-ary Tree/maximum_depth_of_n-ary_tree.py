"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# simple tree problem
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        maximum_depth = 0
        for c in root.children:
            maximum_depth = max(maximum_depth, self.maxDepth(c))
        return maximum_depth + 1
