# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # if it's an empty tree, just return False
        if not root:
            return False

        # store (target - value)
        table = [k - root.val]

        return self.searchTree(root.left, table, k) or self.searchTree(root.right, table, k)

    def searchTree(self, root: Optional[TreeNode], table: List, k: int) -> bool:
        if not root:
            return

        if root.val in table:
            # if find two sum solution, return True
            return True
        else:
            # else put (target - value) into our table
            table.append(k - root.val)

        return self.searchTree(root.left, table, k) or self.searchTree(root.right, table, k)
