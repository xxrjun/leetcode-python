# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, leftNode: Optional[TreeNode], rightNode: Optional[TreeNode]):
        if not leftNode or not rightNode:
            return leftNode == rightNode

        if leftNode.val != rightNode.val:
            return False

        return self.isSymmetricHelper(leftNode.left, rightNode.right) and self.isSymmetricHelper(leftNode.right, rightNode.left)
