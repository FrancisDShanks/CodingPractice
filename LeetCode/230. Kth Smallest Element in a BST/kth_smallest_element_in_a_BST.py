# 根据中序遍历找第k个,找到就返回
# follow up的情况,BST频繁更新,可以在中序遍历时候存下前k个为counts,然后更新这个counts
'''
这道题的 Follow up 中说假设该 BST 被修改的很频繁，而且查找第k小元素的操作也很频繁，问我们如何优化。
其实最好的方法还是像上面的解法那样利用分治法来快速定位目标所在的位置，
但是每个递归都遍历左子树所有结点来计算个数的操作并不高效，
所以应该修改原树结点的结构，使其保存包括当前结点和其左右子树所有结点的个数，这样就可以快速得到任何左子树结点总数来快速定位目标值了。
定义了新结点结构体，然后就要生成新树，还是用递归的方法生成新树，注意生成的结点的 count 值要累加其左右子结点的 count 值。
然后在求第k小元素的函数中，先生成新的树，然后调用递归函数。
在递归函数中，不能直接访问左子结点的 count 值，因为左子节结点不一定存在，所以要先判断，如果左子结点存在的话，那么跟上面解法的操作相同。
如果不存在的话，当此时k为1的时候，直接返回当前结点值，否则就对右子结点调用递归函数，k自减1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        s = list()
        cur = root
        cnt = 0
        while s or cur:
            if not cur: 
                cur = s.pop()
            else:
                while cur.left:
                    s.append(cur)
                    cur = cur.left
            
            cnt += 1
            if cnt == k:
                return cur.val
            
            cur = cur.right
        
            
            
        
