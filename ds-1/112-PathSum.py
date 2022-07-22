# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, curSum=0, targetSum=targetSum)

    def helper(self, root, curSum, targetSum) -> bool:
        if not root:
            return False

        curSum += root.val

        # Reach leaf node
        if not root.left and not root.right:
            return curSum == targetSum

        return self.helper(root.left, curSum, targetSum) or self.helper(root.right, curSum, targetSum)
