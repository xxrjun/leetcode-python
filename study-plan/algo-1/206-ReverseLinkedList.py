# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curFront = None

        while head.next:
            cur = head
            head = head.next
            cur.next = curFront
            curFront = cur

        head.next = curFront

        return head
