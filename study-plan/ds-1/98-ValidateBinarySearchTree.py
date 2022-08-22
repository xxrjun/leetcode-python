# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree = []
        self.inorder(root, tree)

        for i in range(1, len(tree)):
            if tree[i - 1] >= tree[i]:
                return False

        return True

    def inorder(self, root: Optional[TreeNode], tree: List[TreeNode]) -> None:
        if not root:
            return

        self.inorder(root.left, tree)
        tree.append(root.val)
        self.inorder(root.right, tree)
