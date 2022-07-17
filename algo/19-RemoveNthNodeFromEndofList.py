# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        listlen = 0

        # Calculate the length of list
        while cur != None:
            cur = cur.next
            listlen += 1


        if listlen == n:
            return head.next

        cur = head
        # Iterate to the front of place should be remove
        for i in range(listlen - n - 1):
            cur = cur.next

        # Remove specific
        if cur.next != None:
            cur.next = cur.next.next
        else:
            cur.next = None

        return head