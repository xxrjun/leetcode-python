# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val < val:
            # if root.val is smaller than val, then search right subtree
            return self.searchBST(root.right, val)
        else:
            # if root.val is larger than val, then search left subtree
            return self.searchBST(root.left, val)
