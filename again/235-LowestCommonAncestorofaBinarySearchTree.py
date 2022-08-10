# 235. Lowest Common Ancestor of a Binary Search Tree
# Idea:
#       因為要介於 p, q 之間，所以只要大於 p 跟 q 或小於 p 跟 q，就應該繼續往下找

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
