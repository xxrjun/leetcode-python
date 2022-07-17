# 141. Linked List Cycle

# Solution 1: Two Pointers (Faster: O(n/2), Less memory usage)
# Solution 2: Rewrite visited Node (O(n), Less memory usage)
# Solution 3: Hash Table (Slower: O(n), More memory usage)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # Solution 1: Two Pointers (Faster: O(n/2), Less memory usage)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head  # Initialize two pointers

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Has cycle
                return True

        return False

    # Solution 2: Rewrite visited Node (O(n), Less memory usage)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head

        while cur:
            if cur.val == "v":  # v: visited
                return True

            cur.val = "v"  # rewrite visited node

            cur = cur.next

        return False

    # Solution 3: Hash Table (Slow: O(n), More memory usage)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashTable = {}  # (node, position)
        countIndex = 0

        cur = head
        while cur != None:
            # Has cycle
            if cur in hashTable.keys():
                return True

            #  Put node into hash table
            hashTable[cur] = countIndex
            countIndex += 1

            cur = cur.next

        return False