# 116. Populating Next Right Pointers in Each Node

# Definition for a Node.

from asyncio.windows_events import NULL


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return []

        treeList = []
        index = 1
        while root:
            if root.right.val == 2 * index + 1:
                root.next = Node(None)
            else:
                root.left.next = root.right

        return treeList

    def preorderTraversal(self, root: 'Optional[Node]', index) -> 'Optional[Node]':
        if not root:
            return []

        return root + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
