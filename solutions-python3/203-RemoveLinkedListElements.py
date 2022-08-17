# 203. Remove Linked List Elements


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:

        # Remove front elements == val
        cur = head
        while cur and cur.val == val:
            cur = cur.next

        if cur == None:
            return None

        # Remove other elements == val
        head = cur
        slow, fast = head, head.next

        while fast:
            if fast.val == val:
                fast = fast.next
                slow.next = fast
            else:
                fast = fast.next
                slow = slow.next

        return head
