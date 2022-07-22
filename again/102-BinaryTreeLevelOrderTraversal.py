# 102. Binary Tree Level Order Traversal

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root if null, just return an empty list
        if not root:
            return []

        # result should be return
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            # a list to store value of nodes in current level
            curLevelNodes = []

            # loop through our queue
            for i in range(len(q)):
                # get the node front of queue
                node = q.popleft()

                if node:
                    # if node exists, add it to the current list
                    curLevelNodes.append(node.val)

                    # add children nodes to our queue if exist
                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            # add the current list to our result
            res += [curLevelNodes]

        return res
